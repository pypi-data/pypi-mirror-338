import ctypes
import json
from ..lib import get_lib

lib = get_lib()

# Callback function type for instruct responses
RESPONSE_CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p)

# Define function prototypes
lib.RAPID_Core_InstructStandard_Create.argtypes = [ctypes.c_void_p, RESPONSE_CALLBACK, ctypes.c_void_p]
lib.RAPID_Core_InstructStandard_Create.restype = ctypes.c_void_p

lib.RAPID_Core_InstructStandard_Request.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
lib.RAPID_Core_InstructStandard_Request.restype = None

lib.RAPID_Core_InstructStandard_Release.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_InstructStandard_Release.restype = None

lib.RAPID_Core_InstructStandard_SetResponseSendPort.argtypes = [ctypes.c_void_p, ctypes.c_longlong]
lib.RAPID_Core_InstructStandard_SetResponseSendPort.restype = None

class InstructState:
    RESPONSE_SUCCESS = 0
    TRANSPORT_UNAVAILABLE = 1
    RESPONSE_TIMEOUT = 2
    DUPLICATE_INSTRUCT = 3
    FAILED_INSTRUCT = 4
    UNKNOWN = 5
    DEVICE_IN_PROGRESS = 6
    DEVICE_ERROR_HEADER = 7
    DEVICE_UNSUPPORT_CMD = 8
    DEVICE_INVALID_PARAM = 9
    DEVICE_LACK_OF_RESOURCE = 10
    DEVICE_ERROR_INTERNAL = 11
    DEVICE_NOT_ALLOWED = 12

class Instruct:
    def __init__(self, pipe_proxy, callback=None):
        """
        Initialize an instruction channel with the given pipe proxy.
        
        Args:
            pipe_proxy: The pipe proxy object to use for communication
            callback (callable, optional): Callback function for responses
        """
        self._callbacks = {}
        self._callback_id = 0
        self._handle = None
        
        if not pipe_proxy or not hasattr(pipe_proxy, '_handle'):
            raise ValueError("Invalid pipe_proxy provided")
        
        # Create C callback function
        @RESPONSE_CALLBACK
        def response_callback(json_str, json_length, user_data):
            if not json_str:
                return
            
            try:
                json_data = json_str[:json_length].decode('utf-8')
                data = json.loads(json_data)
                
                # Call user callback if provided
                if callback:
                    callback(data)
                
                # Call specific callback if registered
                callback_id = ctypes.cast(user_data, ctypes.POINTER(ctypes.c_int)).contents.value
                if callback_id in self._callbacks:
                    self._callbacks[callback_id](data)
            except Exception as e:
                print(f"Error in response callback: {e}")
        
        self._c_callback = response_callback
        self._user_data = ctypes.c_int(0)
        self._handle = lib.RAPID_Core_InstructStandard_Create(
            pipe_proxy._handle, 
            self._c_callback, 
            ctypes.byref(self._user_data)
        )
    
    def __del__(self):
        """Clean up resources when object is destroyed"""
        self.release()
    
    def request(self, name, params, callback=None):
        """
        Send an instruction request.
        
        Args:
            name (str): The instruction name
            params (dict or str): The instruction parameters
            callback (callable, optional): Callback function for this specific request
            
        Returns:
            int: A callback ID if callback was provided, otherwise None
        """
        if not self._handle:
            raise RuntimeError("Instruct object has been released")
        
        name_bytes = name.encode('utf-8') if name else None
        
        # Handle parameter conversion
        if isinstance(params, dict):
            params_str = json.dumps(params)
        elif isinstance(params, str):
            params_str = params
        else:
            params_str = "{}"
        
        params_bytes = params_str.encode('utf-8')
        
        # Register callback if provided
        callback_id = None
        if callback:
            self._callback_id += 1
            callback_id = self._callback_id
            self._callbacks[callback_id] = callback
            self._user_data = ctypes.c_int(callback_id)
        
        lib.RAPID_Core_InstructStandard_Request(self._handle, name_bytes, params_bytes)
        return callback_id
    
    def set_response_send_port(self, port):
        """
        Set the port for sending responses.
        
        Args:
            port (int): The port number
        """
        if not self._handle:
            raise RuntimeError("Instruct object has been released")
        
        lib.RAPID_Core_InstructStandard_SetResponseSendPort(self._handle, port)
    
    def release(self):
        """Release the instruction channel resources"""
        if self._handle:
            lib.RAPID_Core_InstructStandard_Release(self._handle)
            self._handle = None
            self._callbacks.clear() 