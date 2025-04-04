"""
RAPID Kit Python SDK
"""
import os
import sys

from .core import Core
from .media import MediaPlayer, MediaChat, RGBFormat, set_rgb_pixel_format
from .sdl import (
    create_aout_for_audio_queue,
    create_ain_for_audio_toolbox,
    create_silence_vout,
    create_silence_aout,
    create_vout_simple_callback,
    VoutFrameCallback
)

__version__ = "0.1.0"

__all__ = [
    'Core', 
    'MediaPlayer', 
    'MediaChat', 
    'RGBFormat', 
    'set_rgb_pixel_format',
    'create_aout_for_audio_queue',
    'create_ain_for_audio_toolbox',
    'create_silence_vout',
    'create_silence_aout',
    'create_vout_simple_callback',
    'VoutFrameCallback'
]
