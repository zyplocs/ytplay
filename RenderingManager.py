import cv2


class RenderingManager:
    """ASCII chars from darkest to lightest for converting \
    grayscale to ASCII."""

    _ASCII_CHARS = "@%#*+=:. "

    def convert_frame_to_ascii(self, frame, scale_factor, max_frame_width):
        """
        Convert a video frame to an ASCII representation.

        Args:
            frame: The input video frame (numpy array)
            scale_factor (float): Scaling factor for adjusting the frame size
            max_frame_width (int): Maximum width of the ASCII representation

        Returns:
            str: The ASCII representation of the frame
        """
        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calculate the width of the ASCII frame
        cols = gray_frame.shape[1]
        rows = gray_frame.shape[0]
        width = int(cols * scale_factor)

        # Enforce max_frame_width if specified
        if max_frame_width > 0:
            width = min(width, max_frame_width)

        # Maintain aspect ratio for ASCII art
        aspect_ratio = cols / rows
        height = int(width / aspect_ratio)

        # Resize the grayscale frame
        resized_frame = cv2.resize(gray_frame, (width, height))

        # Convert each pixel to an ASCII character
        ascii_frame = ""
        for row in resized_frame:
            for pixel in row:
                intensity = int(pixel / 255 * (len(self._ASCII_CHARS) - 1))
                ascii_frame += self._ASCII_CHARS[intensity]
            ascii_frame += "\n"

        return ascii_frame
