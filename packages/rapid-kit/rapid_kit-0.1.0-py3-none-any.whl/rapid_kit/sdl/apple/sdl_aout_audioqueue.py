import ctypes
from ...lib import get_sdl_lib

lib = get_sdl_lib()

# Define function prototypes
lib.RAPID_SDL_Aout_CreateForAudioQueue.argtypes = []
lib.RAPID_SDL_Aout_CreateForAudioQueue.restype = ctypes.c_void_p

def create_aout_for_audio_queue():
    """
    Create an audio output device using Apple's AudioQueue.
    
    Returns:
        int: Handle to the audio output device
    """
    return lib.RAPID_SDL_Aout_CreateForAudioQueue() 