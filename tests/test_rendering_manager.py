import numpy as np
from RenderingManager import RenderingManager


def test_convert_frame_to_ascii():
    # Create a 2x2 BGR image with increasing brightness
    frame = np.array(
        [
            [[0, 0, 0], [128, 128, 128]],
            [[192, 192, 192], [255, 255, 255]],
        ],
        dtype=np.uint8,
    )

    manager = RenderingManager()
    ascii_art = manager.convert_frame_to_ascii(frame, scale_factor=1.0, max_frame_width=0)

    assert ascii_art == "@+\n: \n"
