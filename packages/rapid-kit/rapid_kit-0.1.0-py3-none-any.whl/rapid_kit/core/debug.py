import ctypes
from ..lib import get_lib

lib = get_lib()

# Define function prototypes
lib.RAPID_Core_DebuggingCode_Create.argtypes = []
lib.RAPID_Core_DebuggingCode_Create.restype = ctypes.c_char_p

lib.RAPID_Core_DebuggingCode_Free.argtypes = [ctypes.c_char_p]
lib.RAPID_Core_DebuggingCode_Free.restype = None

lib.RAPID_Core_DebuggingCode_Apply.argtypes = [ctypes.c_char_p]
lib.RAPID_Core_DebuggingCode_Apply.restype = ctypes.c_int

class Debug:
    @staticmethod
    def create_debugging_code():
        """
        Create a debugging code.
        
        Returns:
            str: The generated debugging code
        """
        code_ptr = lib.RAPID_Core_DebuggingCode_Create()
        if not code_ptr:
            return None
        
        code = code_ptr.decode('utf-8')
        lib.RAPID_Core_DebuggingCode_Free(code_ptr)
        return code
    
    @staticmethod
    def apply_debugging_code(code):
        """
        Apply a debugging code.
        
        Args:
            code (str): The debugging code to apply
            
        Returns:
            bool: True if the code was applied successfully, False otherwise
        """
        if not code:
            return False
        
        code_bytes = code.encode('utf-8')
        result = lib.RAPID_Core_DebuggingCode_Apply(code_bytes)
        return result != 0 