import ctypes
from ..lib import get_lib

lib = get_lib()

# Define global variables for previous crash details
lib.previous_crash_detail = ctypes.c_char_p.in_dll(lib, "previous_crash_detail")
lib.previous_crash_detail_length = ctypes.c_int.in_dll(lib, "previous_crash_detail_length")

# Define function prototypes
lib.RAPID_Core_RegisterSignalHandler.argtypes = []
lib.RAPID_Core_RegisterSignalHandler.restype = None

def get_previous_crash_detail():
    """
    Get details about the previous crash, if any.
    
    Returns:
        str: The crash details, or None if there was no crash
    """
    if not lib.previous_crash_detail or lib.previous_crash_detail_length.value <= 0:
        return None
    
    return lib.previous_crash_detail.value[:lib.previous_crash_detail_length.value].decode('utf-8')

def register_signal_handler():
    """Register a signal handler for crash detection"""
    lib.RAPID_Core_RegisterSignalHandler() 