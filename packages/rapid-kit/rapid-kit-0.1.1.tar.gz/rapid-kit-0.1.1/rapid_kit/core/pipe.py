import ctypes
from ..lib import get_lib

lib = get_lib()

# Callback function types
PIPE_STATE_CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_void_p)
INSTRUCT_RESPONSE_CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p)

# Define function prototypes
lib.RAPID_Core_PipeProxy_Create.argtypes = [ctypes.c_char_p]
lib.RAPID_Core_PipeProxy_Create.restype = ctypes.c_void_p

lib.RAPID_Core_PipeProxy_Destroy.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_PipeProxy_Destroy.restype = None

lib.RAPID_Core_PipeProxy_Establish.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_PipeProxy_Establish.restype = None

lib.RAPID_Core_PipeProxy_Abolish.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_PipeProxy_Abolish.restype = None

lib.RAPID_Core_PipeProxy_Status.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_PipeProxy_Status.restype = ctypes.c_int

lib.RAPID_Core_PipeProxy_EnableLanMode.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.RAPID_Core_PipeProxy_EnableLanMode.restype = None

lib.RAPID_Core_PipeProxy_SetStatusFunc.argtypes = [ctypes.c_void_p, PIPE_STATE_CALLBACK, ctypes.c_void_p]
lib.RAPID_Core_PipeProxy_SetStatusFunc.restype = None

lib.RAPID_Core_PipeProxy_SetStatusSendPort.argtypes = [ctypes.c_void_p, ctypes.c_longlong]
lib.RAPID_Core_PipeProxy_SetStatusSendPort.restype = None

lib.RAPID_Core_PipeProxy_InstructRequest.argtypes = [
    ctypes.c_void_p, ctypes.c_uint, ctypes.c_char_p, ctypes.c_uint,
    INSTRUCT_RESPONSE_CALLBACK, ctypes.c_uint, ctypes.c_void_p
]
lib.RAPID_Core_PipeProxy_InstructRequest.restype = None

lib.RAPID_Core_PipeProxy_InstructRequest_ResponseBySendPort.argtypes = [
    ctypes.c_void_p, ctypes.c_uint, ctypes.c_char_p, ctypes.c_uint,
    ctypes.c_longlong, ctypes.c_uint
]
lib.RAPID_Core_PipeProxy_InstructRequest_ResponseBySendPort.restype = None

lib.RAPID_Core_PipeToken_Prepare.argtypes = [ctypes.c_char_p]
lib.RAPID_Core_PipeToken_Prepare.restype = None

class PipeProxy:
    def __init__(self, device_id):
        """
        Initialize a pipe proxy for communication with a device.
        
        Args:
            device_id (str): The ID of the device to connect to
        """
        self._callbacks = {}
        self._callback_id = 0
        device_id_bytes = device_id.encode('utf-8') if device_id else None
        self._handle = lib.RAPID_Core_PipeProxy_Create(device_id_bytes)
        if not self._handle:
            raise RuntimeError("Failed to create pipe proxy")
        
        self._state_callback = None
        self._user_data = None
    
    def __del__(self):
        """Clean up resources when object is destroyed"""
        self.destroy()
    
    def establish(self):
        """Establish a connection to the device"""
        if not self._handle:
            raise RuntimeError("Pipe proxy has been destroyed")
        
        lib.RAPID_Core_PipeProxy_Establish(self._handle)
    
    def abolish(self):
        """Terminate the connection to the device"""
        if not self._handle:
            raise RuntimeError("Pipe proxy has been destroyed")
        
        lib.RAPID_Core_PipeProxy_Abolish(self._handle)
    
    def get_status(self):
        """
        Get the current connection status.
        
        Returns:
            int: The connection status code
        """
        if not self._handle:
            raise RuntimeError("Pipe proxy has been destroyed")
        
        return lib.RAPID_Core_PipeProxy_Status(self._handle)
    
    def enable_lan_mode(self, enabled=True):
        """
        Enable or disable LAN mode.
        
        Args:
            enabled (bool): Whether to enable LAN mode
        """
        if not self._handle:
            raise RuntimeError("Pipe proxy has been destroyed")
        
        lib.RAPID_Core_PipeProxy_EnableLanMode(self._handle, 1 if enabled else 0)
    
    def set_status_callback(self, callback):
        """
        Set a callback function for status changes.
        
        Args:
            callback (callable): A function taking (status) as parameter
        """
        if not self._handle:
            raise RuntimeError("Pipe proxy has been destroyed")
        
        # Create C callback function
        @PIPE_STATE_CALLBACK
        def state_callback(status, user_data):
            if callback:
                try:
                    callback(status)
                except Exception as e:
                    print(f"Error in pipe state callback: {e}")
        
        self._state_callback = state_callback
        lib.RAPID_Core_PipeProxy_SetStatusFunc(self._handle, self._state_callback, None)
    
    def set_status_send_port(self, port):
        """
        Set the port for sending status updates.
        
        Args:
            port (int): The port number
        """
        if not self._handle:
            raise RuntimeError("Pipe proxy has been destroyed")
        
        lib.RAPID_Core_PipeProxy_SetStatusSendPort(self._handle, port)
    
    def instruct_request(self, instruct_id, buffer, timeout_s=10, callback=None):
        """
        Send an instruction request.
        
        Args:
            instruct_id (int): The instruction ID
            buffer (str or bytes): The instruction buffer
            timeout_s (int): Timeout in seconds
            callback (callable, optional): Callback function for the response
            
        Returns:
            int: A callback ID if callback was provided, otherwise None
        """
        if not self._handle:
            raise RuntimeError("Pipe proxy has been destroyed")
        
        # Convert buffer to bytes if it's a string
        if isinstance(buffer, str):
            buffer_bytes = buffer.encode('utf-8')
        elif isinstance(buffer, bytes):
            buffer_bytes = buffer
        else:
            raise ValueError("Buffer must be a string or bytes")
        
        buffer_size = len(buffer_bytes)
        
        if callback:
            # Register callback
            self._callback_id += 1
            callback_id = self._callback_id
            
            @INSTRUCT_RESPONSE_CALLBACK
            def response_callback(state, response_buffer, buffer_size, user_data):
                try:
                    data = None
                    if response_buffer and buffer_size > 0:
                        data = response_buffer[:buffer_size].decode('utf-8')
                    callback(state, data)
                except Exception as e:
                    print(f"Error in instruct response callback: {e}")
            
            self._callbacks[callback_id] = response_callback
            
            lib.RAPID_Core_PipeProxy_InstructRequest(
                self._handle, instruct_id, buffer_bytes, buffer_size,
                response_callback, timeout_s, None
            )
            
            return callback_id
        else:
            return None
    
    def instruct_request_with_send_port(self, instruct_id, buffer, send_port, timeout_s=10):
        """
        Send an instruction request with a response send port.
        
        Args:
            instruct_id (int): The instruction ID
            buffer (str or bytes): The instruction buffer
            send_port (int): The port to send the response to
            timeout_s (int): Timeout in seconds
        """
        if not self._handle:
            raise RuntimeError("Pipe proxy has been destroyed")
        
        # Convert buffer to bytes if it's a string
        if isinstance(buffer, str):
            buffer_bytes = buffer.encode('utf-8')
        elif isinstance(buffer, bytes):
            buffer_bytes = buffer
        else:
            raise ValueError("Buffer must be a string or bytes")
        
        buffer_size = len(buffer_bytes)
        
        lib.RAPID_Core_PipeProxy_InstructRequest_ResponseBySendPort(
            self._handle, instruct_id, buffer_bytes, buffer_size,
            send_port, timeout_s
        )
    
    def destroy(self):
        """Release the pipe proxy resources"""
        if self._handle:
            lib.RAPID_Core_PipeProxy_Destroy(self._handle)
            self._handle = None
            self._callbacks.clear()
            self._state_callback = None

def prepare_pipe_token(device_id):
    """
    Prepare a token for pipe connection.
    
    Args:
        device_id (str): The device ID
    """
    if not device_id:
        return
    
    device_id_bytes = device_id.encode('utf-8')
    lib.RAPID_Core_PipeToken_Prepare(device_id_bytes) 