import cv2
import yt_dlp


class VideoStreamManager:
    """yt-dlp options for extracting video metadata."""

    _yt_dlp_opts = {"quiet": True, "retries": 99, "noprocess": True, "format": "worst"}

    def get_video_metadata(self, video_url):
        """
        Extract video metadata (like the stream URL) using yt-dlp.

        Parameters
        ----------
        - video_url (str): The URL of the video

        Returns
        -------
        dict: A dictionary containing the stream URL
        """
        ytdl = yt_dlp.YoutubeDL(self._yt_dlp_opts)
        video_info = ytdl.extract_info(video_url, download=False)

        return {"stream_url": video_info["url"]}

    def parse_video_stream(self, stream_url, frame_callback):
        """
        Read frames from a video stream and processes them using\
        a callback function.

        Parameters
        ----------
        - stream_url (str): The URL of the video stream
        - frame_callback (function): A function to process each video frame
        """
        cv2_capture = cv2.VideoCapture(stream_url)

        while True:
            ret, frame = cv2_capture.read()
            if not ret or frame is None:
                break

            frame_callback(frame)

        cv2_capture.release()
