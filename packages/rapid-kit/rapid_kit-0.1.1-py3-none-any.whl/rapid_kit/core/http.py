import ctypes
from ..lib import get_lib

lib = get_lib()

class HttpResp(ctypes.Structure):
    _fields_ = [
        ("data", ctypes.c_char_p),
        ("success", ctypes.c_int),
        ("message", ctypes.c_char_p),
        ("code", ctypes.c_int)
    ]

# Define function prototypes
lib.RAPID_Core_HttpRequest.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p]
lib.RAPID_Core_HttpRequest.restype = ctypes.POINTER(HttpResp)

lib.RAPID_Core_HttpResp_Free.argtypes = [ctypes.POINTER(HttpResp)]
lib.RAPID_Core_HttpResp_Free.restype = None

class Http:
    # HTTP method constants
    GET = 0
    POST = 1
    PUT = 2
    DELETE = 3
    
    @staticmethod
    def request(path, method=GET, content=None):
        """
        Make an HTTP request.
        
        Args:
            path (str): The URL path for the request
            method (int): The HTTP method (Http.GET, Http.POST, Http.PUT, Http.DELETE)
            content (str, optional): The request body content
            
        Returns:
            dict: Response containing data, success, message, and code
        """
        path_bytes = path.encode('utf-8') if path else None
        content_bytes = content.encode('utf-8') if content else None
        
        resp_ptr = lib.RAPID_Core_HttpRequest(path_bytes, method, content_bytes)
        
        if not resp_ptr:
            return None
        
        resp = resp_ptr.contents
        result = {
            'data': resp.data.decode('utf-8') if resp.data else None,
            'success': bool(resp.success),
            'message': resp.message.decode('utf-8') if resp.message else None,
            'code': resp.code
        }
        
        lib.RAPID_Core_HttpResp_Free(resp_ptr)
        return result 