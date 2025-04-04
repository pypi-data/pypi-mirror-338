import ctypes
from ...lib import get_sdl_lib

lib = get_sdl_lib()

# Define VoutOverlay structure for future use
class VoutOverlay(ctypes.Structure):
    pass

# Define callback function type
VoutFrameCallback = ctypes.CFUNCTYPE(None, ctypes.POINTER(VoutOverlay), ctypes.c_void_p)

# Define function prototypes
lib.RAPID_SDL_Vout_SimpleCallback_Create.argtypes = [VoutFrameCallback, ctypes.c_void_p]
lib.RAPID_SDL_Vout_SimpleCallback_Create.restype = ctypes.c_void_p

def create_vout_simple_callback(callback, user_data=None):
    """
    Create a video output device with a frame callback.
    
    Args:
        callback (callable): Function to call for each video frame
        user_data (object, optional): User data to pass to the callback
        
    Returns:
        int: Handle to the video output device
    """
    # Store callback reference to prevent garbage collection
    global _stored_callbacks
    if not hasattr(create_vout_simple_callback, '_stored_callbacks'):
        create_vout_simple_callback._stored_callbacks = {}
    
    # Create C callback function
    @VoutFrameCallback
    def frame_callback_wrapper(overlay, user_data_ptr):
        try:
            if callback:
                callback(overlay, user_data)
        except Exception as e:
            print(f"Error in video frame callback: {e}")
    
    # Store reference
    callback_id = id(callback)
    create_vout_simple_callback._stored_callbacks[callback_id] = frame_callback_wrapper
    
    # Create the video output device
    return lib.RAPID_SDL_Vout_SimpleCallback_Create(frame_callback_wrapper, ctypes.c_void_p()) 