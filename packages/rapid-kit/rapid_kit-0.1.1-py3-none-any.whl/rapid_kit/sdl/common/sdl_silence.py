import ctypes
from ...lib import get_sdl_lib

lib = get_sdl_lib()

# Define function prototypes
lib.RAPID_SDL_Vout_Silence_Create.argtypes = []
lib.RAPID_SDL_Vout_Silence_Create.restype = ctypes.c_void_p

lib.RAPID_SDL_Aout_Silence_Create.argtypes = []
lib.RAPID_SDL_Aout_Silence_Create.restype = ctypes.c_void_p

def create_silence_vout():
    """
    Create a silent video output device.
    
    Returns:
        int: Handle to the silent video output device
    """
    return lib.RAPID_SDL_Vout_Silence_Create()

def create_silence_aout():
    """
    Create a silent audio output device.
    
    Returns:
        int: Handle to the silent audio output device
    """
    return lib.RAPID_SDL_Aout_Silence_Create() 