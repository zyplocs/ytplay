from CliManager import CliManager
from service import ServiceLocator


def main():
    """Create main function for ytplay."""
    # Initialize the ServiceLocator
    service_locator = ServiceLocator()

    # Initialize the CliManager with scaling factor and maximum frame width
    cli_manager = CliManager(service_locator, scaling_factor=0.5, max_frame_width=100)

    # Sample video
    video_url = "https://www.youtube.com/watch?v=iWXZh8slA3Q"

    # Render the video as ASCII art in the CLI
    cli_manager.render_video(video_url)


if __name__ == "__main__":
    main()
