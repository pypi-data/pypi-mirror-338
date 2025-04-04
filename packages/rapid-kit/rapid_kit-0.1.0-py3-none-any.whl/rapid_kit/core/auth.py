import ctypes
from ..lib import get_lib

lib = get_lib()

class AuthResp(ctypes.Structure):
    _fields_ = [
        ("user_id", ctypes.c_int),
        ("issue_at", ctypes.c_int),
        ("expires_in", ctypes.c_int),
        ("success", ctypes.c_int),
        ("message", ctypes.c_char_p),
        ("code", ctypes.c_int)
    ]

# Define function prototypes
lib.RAPID_Core_Authenticate.argtypes = [ctypes.c_char_p]
lib.RAPID_Core_Authenticate.restype = ctypes.POINTER(AuthResp)

lib.RAPID_Core_AuthResp_Free.argtypes = [ctypes.POINTER(AuthResp)]
lib.RAPID_Core_AuthResp_Free.restype = None

class Auth:
    @staticmethod
    def authenticate(access_token):
        """
        Authenticate with the given access token.
        
        Args:
            access_token (str): The access token for authentication
            
        Returns:
            dict: Authentication response containing user_id, issue_at, expires_in, 
                  success, message, and code
        """
        token_bytes = access_token.encode('utf-8') if access_token else None
        resp_ptr = lib.RAPID_Core_Authenticate(token_bytes)
        
        if not resp_ptr:
            return None
        
        resp = resp_ptr.contents
        result = {
            'user_id': resp.user_id,
            'issue_at': resp.issue_at,
            'expires_in': resp.expires_in,
            'success': bool(resp.success),
            'message': resp.message.decode('utf-8') if resp.message else None,
            'code': resp.code
        }
        
        lib.RAPID_Core_AuthResp_Free(resp_ptr)
        return result 