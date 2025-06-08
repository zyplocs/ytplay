from unittest.mock import MagicMock, patch

from VideoStreamManager import VideoStreamManager


def test_get_video_metadata():
    expected_stream = "http://test/stream"
    with patch("yt_dlp.YoutubeDL") as MockYDL:
        mock_instance = MockYDL.return_value
        mock_instance.extract_info.return_value = {"url": expected_stream}

        manager = VideoStreamManager()
        metadata = manager.get_video_metadata("https://example.com/video")

        mock_instance.extract_info.assert_called_once_with(
            "https://example.com/video", download=False
        )
        assert metadata == {"stream_url": expected_stream}
