from RenderingManager import RenderingManager
from VideoStreamManager import VideoStreamManager


class DisplayManager:
    """Handle displaying ASCII frames in the CLI."""

    @staticmethod
    def display_frame(frame_data, cli_cols, cli_rows):
        """
        Display an ASCII frame in the CLI.

        Args:
            frame_data (dict): Contains the ASCII frame to be displayed
            cli_cols (int): Number of columns in the terminal
            cli_rows (int): Number of rows in the terminal
        """
        # Clear the terminal before displaying the frame
        print("\033[H\033[J", end="")  # ANSI escape sequence to clear screen

        # Print the ASCII frame
        print(
            frame_data["video_frame"], end="", flush=True
        )  # Print the ASCII art frame to CLI


class ServiceLocator:
    """Provide access to shared services for rendering and video streaming."""

    def __init__(self):
        self.rendering_manager = RenderingManager()
        self.video_stream_manager = VideoStreamManager()
        self.display_manager = DisplayManager()
