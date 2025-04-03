import typing as T

from pupil_labs.neon_recording.stream.imu.imu_pb2 import ImuPacket

from .base import (
    RTSPData,
    RTSPRawStreamer,
    SDPDataNotAvailableError,
    receive_raw_rtsp_data,
)
from .eye_events import (
    BlinkEventData,
    FixationEventData,
    FixationOnsetEventData,
    RTSPEyeEventStreamer,
    receive_eye_events_data,
)
from .gaze import (
    DualMonocularGazeData,
    EyestateGazeData,
    GazeData,
    RTSPGazeStreamer,
    receive_gaze_data,
)
from .imu import RTSPImuStreamer, receive_imu_data
from .video import RTSPVideoFrameStreamer, VideoFrame, receive_video_frames

RTSPStreamerType = T.TypeVar("RTSPStreamerType", bound="RTSPRawStreamer")
"""Type annotation for RTSP Streamer classes"""

__all__ = [
    "GazeData",
    "DualMonocularGazeData",
    "EyestateGazeData",
    "receive_gaze_data",
    "receive_raw_rtsp_data",
    "receive_video_frames",
    "RTSPData",
    "RTSPGazeStreamer",
    "RTSPRawStreamer",
    "RTSPVideoFrameStreamer",
    "SDPDataNotAvailableError",
    "VideoFrame",
    "RTSPImuStreamer",
    "receive_imu_data",
    "ImuPacket",
    "imu_pb2",
    "RTSPEyeEventStreamer",
    "FixationEventData",
    "FixationOnsetEventData",
    "BlinkEventData",
    "receive_eye_events_data",
]
