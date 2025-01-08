import shutil
from service import ServiceLocator


class CliManager:
    def __init__(self, service_locator, scaling_factor, max_frame_width):
        """
        Initialize the CLI Manager.

        Args:
            service_locator (ServiceLocator): Manages shared services like
             rendering and display
            scaling_factor (float): Scaling factor for the video frame
            max_frame_width (int): Maximum width of the video frame in
             characters
        """
        self._service_locator = service_locator
        self._check_cli_window_size()
        self._scaling_factor = scaling_factor
        self._max_frame_width = max_frame_width
        self._display_frame_data = {"video_frame": ""}

    def _check_cli_window_size(self):
        """Determine the terminal's size (columns and rows)."""
        cols, rows = shutil.get_terminal_size()
        self._cli_cols = int(cols)
        self._cli_rows = int(rows)

    def _render_frame_callback(self, frame):
        """
        Create callback function to process and display each video frame.

        Args:
            frame: A single frame of the video
        """
        # Convert the frame to ASCII
        self._display_frame_data["video_frame"] = (
            self._service_locator.rendering_manager.convert_frame_to_ascii(
                frame, self._scaling_factor, self._max_frame_width
            )
        )

        # Display the frame in the CLI
        self._service_locator.display_manager.display_frame(
            self._display_frame_data, self._cli_cols, self._cli_rows
        )

    def render_video(self, url):
        """
        Render video in the CLI.

        Args:
            url (str): The URL of the video to render
        """
        # Get metadata for the video
        video_metadata = self._service_locator.video_stream_manager.get_video_metadata(
            url
        )
        stream_url = video_metadata["stream_url"]

        # Parse the video stream and render each frame using the callback
        self._service_locator.video_stream_manager.parse_video_stream(
            stream_url, frame_callback=self._render_frame_callback
        )
