import ctypes
from ..lib import get_lib

lib = get_lib()

# Define function prototypes
lib.RAPID_Core_ChatChannel_Create.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_ChatChannel_Create.restype = ctypes.c_void_p

lib.RAPID_Core_ChatChannel_Free.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_ChatChannel_Free.restype = None

class Chat:
    def __init__(self, pipe_proxy):
        """
        Initialize a chat channel with the given pipe proxy.
        
        Args:
            pipe_proxy: The pipe proxy object to use for communication
        """
        self._handle = None
        if pipe_proxy and hasattr(pipe_proxy, '_handle'):
            self._handle = lib.RAPID_Core_ChatChannel_Create(pipe_proxy._handle)
        else:
            raise ValueError("Invalid pipe_proxy provided")
    
    def __del__(self):
        """Clean up resources when object is destroyed"""
        self.close()
    
    def close(self):
        """Release the chat channel resources"""
        if self._handle:
            lib.RAPID_Core_ChatChannel_Free(self._handle)
            self._handle = None 