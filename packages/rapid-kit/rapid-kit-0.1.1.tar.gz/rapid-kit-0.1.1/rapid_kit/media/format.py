import ctypes
from enum import IntEnum
from ..lib import get_media_lib

lib = get_media_lib()

class RGBFormat(IntEnum):
    RGBA = 0
    BGRA = 1

lib.RAPID_Media_RGBPixel_SetFormat.argtypes = [ctypes.c_int]
lib.RAPID_Media_RGBPixel_SetFormat.restype = None

def set_rgb_pixel_format(format):
    if not isinstance(format, (int, RGBFormat)):
        raise ValueError("Format must be a RGBFormat enum value")
    
    lib.RAPID_Media_RGBPixel_SetFormat(int(format)) 