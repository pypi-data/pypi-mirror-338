"""Utilities for rendering the environment."""

import logging
from pathlib import Path
from types import TracebackType
from typing import Sequence

import mujoco
import mujoco.viewer
import numpy as np

from kmv.utils.markers import TrackingConfig, TrackingMarker
from kmv.utils.plotting import Plotter
from kmv.utils.saving import save_video
from kmv.utils.transforms import rotation_matrix_from_direction
from kmv.utils.types import CommandValue, ModelCache

logger = logging.getLogger(__name__)


class MujocoViewerHandler:
    def __init__(
        self,
        handle: mujoco.viewer.Handle,
        capture_pixels: bool = False,
        save_path: str | Path | None = None,
        render_width: int = 640,
        render_height: int = 480,
        make_plots: bool = False,
    ) -> None:
        # breakpoint()
        self.handle = handle
        self._markers: list[TrackingMarker] = []
        self._frames: list[np.ndarray] = []
        self._capture_pixels = capture_pixels
        self._save_path = Path(save_path) if save_path is not None else None
        self._renderer = None
        self._model_cache = ModelCache.create(self.handle.m)
        self._initial_z_offset: float | None = None

        self.current_sim_time = 0.0
        self.prev_sim_time = 0.0
        self._total_sim_time_offset = 0.0
        self._total_current_sim_time = 0.0

        # Initialize real-time plots if requested
        self._make_plots = make_plots
        self._plotter = None
        self._start_time = None

        if self._make_plots:
            # Create plotter with appropriate title
            self._plotter = Plotter(window_title="MuJoCo Robot Data Plots")
            self._plotter.start()

        if (self._capture_pixels and self.handle.m is not None) or (self._save_path is not None):
            self._renderer = mujoco.Renderer(self.handle.m, width=render_width, height=render_height)

    def setup_camera(
        self,
        render_distance: float = 5.0,
        render_azimuth: float = 90.0,
        render_elevation: float = -30.0,
        render_lookat: list[float] = [0.0, 0.0, 0.5],
        render_track_body_id: int | None = None,
    ) -> None:
        """Setup the camera with the given configuration.

        Args:
            render_distance: Distance from the camera to the target
            render_azimuth: Azimuth angle of the camera
            render_elevation: Elevation angle of the camera
            render_lookat: Lookat position of the camera
            render_track_body_id: Body ID to track with the camera
        """
        self.handle.cam.distance = render_distance
        self.handle.cam.azimuth = render_azimuth
        self.handle.cam.elevation = render_elevation
        self.handle.cam.lookat[:] = render_lookat

        if render_track_body_id is not None:
            self.handle.cam.trackbodyid = render_track_body_id
            self.handle.cam.type = mujoco.mjtCamera.mjCAMERA_TRACKING

    def add_plot_group(
        self,
        title: str,
        index_mapping: dict[int, str] | None = None,
        y_axis_min: float | None = None,
        y_axis_max: float | None = None,
    ) -> None:
        """Add a plot group to the viewer."""
        if self._plotter is None:
            raise ValueError("Plotter not initialized. Call `make_plots=True` when initializing the viewer.")
        self._plotter.add_plot_group(title, index_mapping, y_axis_min, y_axis_max)

    def update_plot_group(self, title: str, y_values: list[float]) -> None:
        """Update a plot group with new data."""
        if self._plotter is None:
            raise ValueError("Plotter not initialized. Call `make_plots=True` when initializing the viewer.")
        self._plotter.update_plot_group(title, self._total_current_sim_time, y_values)

    def copy_data(self, dst: mujoco.MjData, src: mujoco.MjData) -> None:
        """Copy the data from the source to the destination."""
        dst.ctrl[:] = src.ctrl[:]
        dst.act[:] = src.act[:]
        dst.xfrc_applied[:] = src.xfrc_applied[:]
        dst.qpos[:] = src.qpos[:]
        dst.qvel[:] = src.qvel[:]
        dst.time = src.time

    def clear_markers(self) -> None:
        """Clear all markers from the scene."""
        if self.handle._user_scn is not None:
            # Reset the geom counter to effectively clear all markers
            self.handle._user_scn.ngeom = 0
            self._markers = []

    def add_marker(
        self,
        name: str,
        pos: np.ndarray = np.zeros(3),
        orientation: np.ndarray = np.eye(3),
        color: np.ndarray = np.array([1, 0, 0, 1]),
        scale: np.ndarray = np.array([0.1, 0.1, 0.1]),
        label: str | None = None,
        track_geom_name: str | None = None,
        track_body_name: str | None = None,
        track_x: bool = True,
        track_y: bool = True,
        track_z: bool = True,
        track_rotation: bool = True,
        tracking_offset: np.ndarray = np.array([0, 0, 0]),
        geom: int = mujoco.mjtGeom.mjGEOM_SPHERE,
    ) -> None:
        """Add a marker to be rendered in the scene."""
        target_name = "world"
        target_type = "body"
        if track_geom_name is not None:
            target_name = track_geom_name
            target_type = "geom"
        elif track_body_name is not None:
            target_name = track_body_name
            target_type = "body"

        tracking_cfg = TrackingConfig(
            target_name=target_name,
            target_type=target_type,
            offset=tracking_offset,
            track_x=track_x,
            track_y=track_y,
            track_z=track_z,
            track_rotation=track_rotation,
        )
        self._markers.append(
            TrackingMarker(
                name=name,
                pos=pos,
                orientation=orientation,
                color=color,
                scale=scale,
                label=label,
                geom=geom,
                tracking_cfg=tracking_cfg,
                model_cache=self._model_cache,
            )
        )

    def add_commands(self, commands: dict[str, CommandValue]) -> None:
        if "linear_velocity_command" in commands:
            command_vel = commands["linear_velocity_command"]
            if hasattr(command_vel, "shape") and hasattr(command_vel, "__len__") and len(command_vel) >= 2:
                x_cmd = float(command_vel[0])
                y_cmd = float(command_vel[1])
                # Add separate velocity arrows for the x and y commands.
                self.add_velocity_arrow(
                    command_velocity=x_cmd,
                    base_pos=(0, 0, 1.7),
                    scale=0.1,
                    rgba=(1.0, 0.0, 0.0, 0.8),
                    direction=[1.0, 0.0, 0.0],
                    label=f"X: {x_cmd:.2f}",
                )
                self.add_velocity_arrow(
                    command_velocity=y_cmd,
                    base_pos=(0, 0, 1.5),
                    scale=0.1,
                    rgba=(0.0, 1.0, 0.0, 0.8),
                    direction=[0.0, 1.0, 0.0],
                    label=f"Y: {y_cmd:.2f}",
                )

    def add_velocity_arrow(
        self,
        command_velocity: float,
        base_pos: tuple[float, float, float] = (0, 0, 1.7),
        scale: float = 0.1,
        rgba: tuple[float, float, float, float] = (0, 1.0, 0, 1.0),
        direction: Sequence[float] | None = None,
        label: str | None = None,
    ) -> None:
        """Convenience method for adding a velocity arrow marker.

        Assumes that velocity arrows track the torso geom (or base body) by default.
        """
        # Default to x-axis if direction not provided.
        if direction is None:
            direction = [1.0, 0.0, 0.0]
        if command_velocity < 0:
            direction = [-d for d in direction]
        mat = rotation_matrix_from_direction(np.array(direction))
        length = abs(command_velocity) * scale

        # Use default tracking: track the torso geometry
        tracking_cfg = TrackingConfig(
            target_name="torso",  # default target name
            target_type="geom",  # default target type
            offset=np.array([0.0, 0.0, 0.5]),
            track_x=True,
            track_y=True,
            track_z=False,  # typically velocity arrows are horizontal
            track_rotation=False,
        )
        marker = TrackingMarker(
            name=label if label is not None else f"Vel: {command_velocity:.2f}",
            pos=np.array(base_pos, dtype=float),
            orientation=mat,
            color=np.array(rgba, dtype=float),
            scale=np.array((0.02, 0.02, max(0.001, length)), dtype=float),
            label=label if label is not None else f"Vel: {command_velocity:.2f}",
            geom=mujoco.mjtGeom.mjGEOM_ARROW,
            tracking_cfg=tracking_cfg,
            model_cache=self._model_cache,
        )
        self._markers.append(marker)

    def _update_scene_markers(self) -> None:
        """Add all current markers to the scene."""
        if self.handle._user_scn is None:
            return

        # Update tracked markers with current positions
        for marker in self._markers:
            marker.update(self.handle.m, self.handle.d)

        # Apply all markers to the scene
        self._apply_markers_to_scene(self.handle._user_scn)

    def add_debug_markers(self) -> None:
        """Add debug markers to the scene using the tracked marker system.

        This adds a sphere at a fixed z height above the robot's base position,
        but following the x,y position of the base.
        """
        if self.handle.d is None:
            return

        # Get the base position from qpos (first 3 values are xyz position)
        base_pos = self.handle.d.qpos[:3].copy()

        # On first call, establish the fixed z height (original z + 0.5)
        if self._initial_z_offset is None:
            self._initial_z_offset = base_pos[2] + 0.5
            print(f"Set fixed z height to: {self._initial_z_offset}")

        # Using the new marker system
        self.add_marker(
            name="debug_marker",
            pos=np.array([base_pos[0], base_pos[1], self._initial_z_offset]),
            scale=np.array([0.1, 0.1, 0.1]),  # Bigger sphere for visibility
            color=np.array([1.0, 0.0, 1.0, 0.8]),  # Magenta color for visibility
            label="Base Pos (fixed z)",
            track_body_name="torso",  # Track the torso body
            track_x=True,
            track_y=True,
            track_z=True,  # Don't track z, keep it fixed
            tracking_offset=np.array([0, 0, 0.5]),  # Offset above the torso
            geom=mujoco.mjtGeom.mjGEOM_ARROW,  # Specify the geom type
        )

        # Print position to console for debugging
        print(f"Marker position: x,y=({base_pos[0]:.2f},{base_pos[1]:.2f}), fixed z={self._initial_z_offset:.2f}")

    def _apply_markers_to_scene(self, scene: mujoco.MjvScene) -> None:
        """Apply markers to the provided scene.

        Args:
            scene: The MjvScene to apply markers to
        """
        for marker in self._markers:
            marker.apply_to_scene(scene)

    def sync(self) -> None:
        """Sync the viewer with current state."""
        self.handle.sync()

    def get_camera(self) -> mujoco.MjvCamera:
        """Get a camera instance configured with current settings."""
        camera = mujoco.MjvCamera()
        camera.type = self.handle.cam.type
        camera.fixedcamid = self.handle.cam.fixedcamid
        camera.trackbodyid = self.handle.cam.trackbodyid
        camera.lookat[:] = self.handle.cam.lookat
        camera.distance = self.handle.cam.distance
        camera.azimuth = self.handle.cam.azimuth
        camera.elevation = self.handle.cam.elevation
        return camera

    def read_pixels(self) -> np.ndarray:
        """Read the current viewport pixels as a numpy array."""
        # Initialize or update the renderer if needed
        if self._renderer is None:
            raise ValueError(
                "Renderer not initialized. "
                "For off-screen rendering, initialize with `capture_pixels=True` or `save_path`"
            )
        # Force a sync to ensure the current state is displayed
        self.handle.sync()

        # Get the current model and data from the handle
        model = self.handle.m
        data = self.handle.d

        if model is None or data is None:
            # If model or data is not available, return empty array with render dimensions
            return np.zeros((self._renderer.height, self._renderer.width, 3), dtype=np.uint8)

        # Get the current camera settings from the viewer
        camera = self.get_camera()

        # Update the scene with the current physics state
        self._renderer.update_scene(data, camera=camera)

        # Add markers to the scene manually
        self._apply_markers_to_scene(self._renderer.scene)

        # Render the scene
        pixels = self._renderer.render()
        return pixels

    def update_time(self) -> None:
        """Update the time of the viewer."""
        self._current_sim_time = self.handle.d.time
        if self._current_sim_time < self.prev_sim_time:
            self._total_sim_time_offset += self.prev_sim_time
        self._total_current_sim_time = self._current_sim_time + self._total_sim_time_offset
        self.prev_sim_time = self._current_sim_time

    def update_and_sync(self) -> None:
        """Update the marks, sync with viewer, and clear the markers."""
        self.update_time()
        if self._make_plots and self._plotter is not None:
            self._plotter.update_axes()
            self._plotter.render_frame()
        # Update scene markers and sync with viewer
        self._update_scene_markers()
        self.sync()

        # Capture frames if needed
        if self._save_path is not None:
            self._frames.append(self.read_pixels())
        self.clear_markers()

    def close(self) -> None:
        """Close the plotting window if it's open."""
        if self._make_plots and self._plotter is not None:
            self._plotter.close()
            print("Closed plotting window")

    def add_plot(
        self,
        plot_name: str,
        y_label: str = "Value",
        y_axis_min: float = 0.0,
        y_axis_max: float = 1.0,
        group: str | None = None,
    ) -> None:
        """Add a new plot to the viewer with optional group assignment."""
        if not self._make_plots or self._plotter is None:
            return

        self._plotter.add_plot(plot_name, y_label=y_label, y_axis_min=y_axis_min, y_axis_max=y_axis_max, group=group)

    def update_plot(self, plot_name: str, y_value: float) -> None:
        """Update a plot with a new data point."""
        if not self._make_plots or self._plotter is None:
            return

        self._plotter.update_plot(plot_name, self._total_current_sim_time, y_value)


class MujocoViewerHandlerContext:
    def __init__(
        self,
        handle: mujoco.viewer.Handle,
        capture_pixels: bool = False,
        save_path: str | Path | None = None,
        render_width: int = 640,
        render_height: int = 480,
        ctrl_dt: float | None = None,
        make_plots: bool = False,
    ) -> None:
        self.handle = handle
        self.capture_pixels = capture_pixels
        self.save_path = save_path
        self.handler: MujocoViewerHandler | None = None
        self.make_plots = make_plots

        # Options for the renderer.
        self.render_width = render_width
        self.render_height = render_height
        self.ctrl_dt = ctrl_dt

    def __enter__(self) -> MujocoViewerHandler:
        self.handler = MujocoViewerHandler(
            self.handle,
            capture_pixels=self.capture_pixels,
            save_path=self.save_path,
            render_width=self.render_width,
            render_height=self.render_height,
            make_plots=self.make_plots,
        )
        return self.handler

    def __exit__(self, exc_type: type | None, exc_value: Exception | None, traceback: TracebackType | None) -> None:
        # If we have a handler and a save path, save the video before closing
        if self.handler is not None and self.save_path is not None:
            fps = 30
            if self.ctrl_dt is not None:
                fps = round(1 / float(self.ctrl_dt))
            save_video(self.handler._frames, self.save_path, fps=fps)

        # Always close the handle
        self.handle.close()


def launch_passive(
    model: mujoco.MjModel,
    data: mujoco.MjData,
    show_left_ui: bool = False,
    show_right_ui: bool = False,
    capture_pixels: bool = False,
    save_path: str | Path | None = None,
    render_width: int = 640,
    render_height: int = 480,
    ctrl_dt: float | None = None,
    make_plots: bool = False,
) -> MujocoViewerHandlerContext:
    """Drop-in replacement for mujoco.viewer.launch_passive.

    See https://github.com/google-deepmind/mujoco/blob/main/python/mujoco/viewer.py

    Args:
        model: The MjModel to render
        data: The MjData to render
        show_left_ui: Whether to show the left UI panel
        show_right_ui: Whether to show the right UI panel
        capture_pixels: Whether to capture pixels for video saving
        save_path: Where to save the video (MP4 or GIF)
        render_width: The width of the rendered image
        render_height: The height of the rendered image
        ctrl_dt: The control time step (used to calculate fps)
        make_plots: Whether to show a separate plotting window
    Returns:
        A context manager that handles the MujocoViewer lifecycle
    """
    return MujocoViewerHandlerContext(
        mujoco.viewer.launch_passive(
            model=model,
            data=data,
            show_left_ui=show_left_ui,
            show_right_ui=show_right_ui,
        ),
        capture_pixels=capture_pixels,
        save_path=save_path,
        render_width=render_width,
        render_height=render_height,
        ctrl_dt=ctrl_dt,
        make_plots=make_plots,
    )
