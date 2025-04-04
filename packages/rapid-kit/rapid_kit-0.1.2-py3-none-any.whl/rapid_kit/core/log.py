import ctypes
from enum import IntEnum
from ..lib import get_lib

lib = get_lib()

# Define log levels
class LogLevel(IntEnum):
    UNKNOWN = 0
    DEFAULT = 1
    VERBOSE = 2
    DEBUG = 3
    INFO = 4
    WARN = 5
    ERROR = 6
    FATAL = 7
    SILENT = 8

# Define function prototypes
lib.RAPID_Core_Logging_Print.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
lib.RAPID_Core_Logging_Print.restype = None

lib.RAPID_Core_LeveledLoggingPrint.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p]
lib.RAPID_Core_LeveledLoggingPrint.restype = None

lib.RAPID_Core_UploadLogging.argtypes = []
lib.RAPID_Core_UploadLogging.restype = ctypes.c_char_p

# Callback function type for console logging
CONSOLE_LOGGING_FUNC = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p)

lib.RAPID_Core_SetConsoleLoggingFunc.argtypes = [CONSOLE_LOGGING_FUNC]
lib.RAPID_Core_SetConsoleLoggingFunc.restype = None

def log(level, tag, message):
    """
    Log a message with the specified level and tag.
    
    Args:
        level (LogLevel): The log level
        tag (str): The log tag
        message (str): The log message
    """
    if not isinstance(level, (int, LogLevel)):
        level = LogLevel.INFO
    
    tag_bytes = tag.encode('utf-8') if tag else b"RAPID"
    message_bytes = message.encode('utf-8') if message else b""
    
    lib.RAPID_Core_Logging_Print(level, tag_bytes, message_bytes)

def log_verbose(tag, message):
    """Log a verbose message"""
    log(LogLevel.VERBOSE, tag, message)

def log_debug(tag, message):
    """Log a debug message"""
    log(LogLevel.DEBUG, tag, message)

def log_info(tag, message):
    """Log an info message"""
    log(LogLevel.INFO, tag, message)

def log_warn(tag, message):
    """Log a warning message"""
    log(LogLevel.WARN, tag, message)

def log_error(tag, message):
    """Log an error message"""
    log(LogLevel.ERROR, tag, message)

def log_fatal(tag, message):
    """Log a fatal message"""
    log(LogLevel.FATAL, tag, message)

def leveled_log(level, tag, message):
    """
    Log a message with level information.
    
    Args:
        level (LogLevel): The log level
        tag (str): The log tag
        message (str): The log message
    """
    if not isinstance(level, (int, LogLevel)):
        level = LogLevel.INFO
    
    tag_bytes = tag.encode('utf-8') if tag else b"RAPID"
    message_bytes = message.encode('utf-8') if message else b""
    
    lib.RAPID_Core_LeveledLoggingPrint(level, tag_bytes, message_bytes)

def upload_logging():
    """
    Upload logs to the server.
    
    Returns:
        str: The upload result
    """
    result_ptr = lib.RAPID_Core_UploadLogging()
    if not result_ptr:
        return None
    
    return result_ptr.decode('utf-8')

def set_console_logging_func(callback):
    """
    Set a custom function for console logging.
    
    Args:
        callback (callable): A function taking (level, tag, message) parameters
    """
    @CONSOLE_LOGGING_FUNC
    def console_logging_callback(level, tag, fmt, args):
        if not callback:
            return
        
        try:
            level_val = int(level)
            tag_str = tag.decode('utf-8') if tag else "RAPID"
            fmt_str = fmt.decode('utf-8') if fmt else ""
            
            # We can't properly handle va_list in Python, so we just pass the format string
            callback(level_val, tag_str, fmt_str)
        except Exception as e:
            print(f"Error in console logging callback: {e}")
    
    # Store the callback to prevent garbage collection
    global _console_logging_callback
    _console_logging_callback = console_logging_callback
    
    lib.RAPID_Core_SetConsoleLoggingFunc(_console_logging_callback) 