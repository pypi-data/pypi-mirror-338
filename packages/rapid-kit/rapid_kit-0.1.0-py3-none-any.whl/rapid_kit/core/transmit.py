import ctypes
from ..lib import get_lib

lib = get_lib()

# Callback function type for binding profile transfer
BINDING_PROFILE_TRANSFER_CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int)

# Define function prototypes
lib.RAPID_Core_ProfileTransmitter_Create.argtypes = []
lib.RAPID_Core_ProfileTransmitter_Create.restype = ctypes.c_void_p

lib.RAPID_Core_ProfileTransmitter_Prepare.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
lib.RAPID_Core_ProfileTransmitter_Prepare.restype = None

lib.RAPID_Core_ProfileTransmitter_SetCallback.argtypes = [ctypes.c_void_p, BINDING_PROFILE_TRANSFER_CALLBACK]
lib.RAPID_Core_ProfileTransmitter_SetCallback.restype = None

lib.RAPID_Core_ProfileTransmitter_SetResponseSendPort.argtypes = [ctypes.c_void_p, ctypes.c_longlong]
lib.RAPID_Core_ProfileTransmitter_SetResponseSendPort.restype = None

lib.RAPID_Core_ProfileTransmitter_GetCurrentState.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_ProfileTransmitter_GetCurrentState.restype = ctypes.c_int

lib.RAPID_Core_ProfileTransmitter_Start.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_ProfileTransmitter_Start.restype = None

lib.RAPID_Core_ProfileTransmitter_Stop.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_ProfileTransmitter_Stop.restype = None

lib.RAPID_Core_ProfileTransmitter_Free.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_ProfileTransmitter_Free.restype = None

class ProfileTransmitter:
    def __init__(self):
        """Initialize a profile transmitter for device binding"""
        self._handle = lib.RAPID_Core_ProfileTransmitter_Create()
        if not self._handle:
            raise RuntimeError("Failed to create profile transmitter")
        
        self._callback = None
    
    def __del__(self):
        """Clean up resources when object is destroyed"""
        self.free()
    
    def prepare(self, ssid, password, bind_token):
        """
        Prepare the profile transmitter with binding information.
        
        Args:
            ssid (str): The WiFi SSID
            password (str): The WiFi password
            bind_token (str): The binding token
        """
        if not self._handle:
            raise RuntimeError("Profile transmitter has been freed")
        
        ssid_bytes = ssid.encode('utf-8') if ssid else None
        password_bytes = password.encode('utf-8') if password else None
        token_bytes = bind_token.encode('utf-8') if bind_token else None
        
        lib.RAPID_Core_ProfileTransmitter_Prepare(
            self._handle, ssid_bytes, password_bytes, token_bytes
        )
    
    def set_callback(self, callback):
        """
        Set a callback function for transfer state changes.
        
        Args:
            callback (callable): A function taking (state) as parameter
        """
        if not self._handle:
            raise RuntimeError("Profile transmitter has been freed")
        
        @BINDING_PROFILE_TRANSFER_CALLBACK
        def transfer_callback(state):
            if callback:
                try:
                    callback(state)
                except Exception as e:
                    print(f"Error in profile transfer callback: {e}")
        
        self._callback = transfer_callback
        lib.RAPID_Core_ProfileTransmitter_SetCallback(self._handle, self._callback)
    
    def set_response_send_port(self, port):
        """
        Set the port for sending response updates.
        
        Args:
            port (int): The port number
        """
        if not self._handle:
            raise RuntimeError("Profile transmitter has been freed")
        
        lib.RAPID_Core_ProfileTransmitter_SetResponseSendPort(self._handle, port)
    
    def get_current_state(self):
        """
        Get the current state of the profile transmitter.
        
        Returns:
            int: The current state code
        """
        if not self._handle:
            raise RuntimeError("Profile transmitter has been freed")
        
        return lib.RAPID_Core_ProfileTransmitter_GetCurrentState(self._handle)
    
    def start(self):
        """Start the profile transmission"""
        if not self._handle:
            raise RuntimeError("Profile transmitter has been freed")
        
        lib.RAPID_Core_ProfileTransmitter_Start(self._handle)
    
    def stop(self):
        """Stop the profile transmission"""
        if not self._handle:
            raise RuntimeError("Profile transmitter has been freed")
        
        lib.RAPID_Core_ProfileTransmitter_Stop(self._handle)
    
    def free(self):
        """Release the profile transmitter resources"""
        if self._handle:
            lib.RAPID_Core_ProfileTransmitter_Free(self._handle)
            self._handle = None
            self._callback = None 