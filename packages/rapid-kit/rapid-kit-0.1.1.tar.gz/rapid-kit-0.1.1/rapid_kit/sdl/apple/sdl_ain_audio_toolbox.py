import ctypes
from ...lib import get_sdl_lib

lib = get_sdl_lib()

# Define function prototypes
lib.RAPID_SDL_Ain_CreateForAudioToolbox.argtypes = []
lib.RAPID_SDL_Ain_CreateForAudioToolbox.restype = ctypes.c_void_p

def create_ain_for_audio_toolbox():
    """
    Create an audio input device using Apple's AudioToolbox.
    
    Returns:
        int: Handle to the audio input device
    """
    return lib.RAPID_SDL_Ain_CreateForAudioToolbox() 