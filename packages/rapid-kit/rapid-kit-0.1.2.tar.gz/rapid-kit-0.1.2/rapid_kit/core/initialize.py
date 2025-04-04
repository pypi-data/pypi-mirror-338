import ctypes
import sys
from ..lib import get_lib

lib = get_lib()

# Define function prototypes
lib.RAPID_Core_Initialize.argtypes = [
    ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, 
    ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_int
]
lib.RAPID_Core_Initialize.restype = ctypes.c_int

lib.RAPID_Core_VersionName.argtypes = []
lib.RAPID_Core_VersionName.restype = ctypes.c_char_p

lib.RAPID_Core_BuildId.argtypes = []
lib.RAPID_Core_BuildId.restype = ctypes.c_char_p

lib.RAPID_Core_CommitHash.argtypes = []
lib.RAPID_Core_CommitHash.restype = ctypes.c_char_p

class Core:
    # Environment constants
    ENV_PRODUCTION = 0
    ENV_STAGING = 1
    ENV_DEVELOPMENT = 2
    
    @staticmethod
    def initialize(app_id, package_name, platform='ios', language='zh-cn', 
                  environment=ENV_PRODUCTION, console_logging=True):
        """
        Initialize the RAPID Core library.
        
        Args:
            app_id (str): The application ID
            package_name (str): The package name
            platform (str, optional): The platform name, defaults to 'ios'
            language (str, optional): The language code, defaults to 'zh-cn'
            environment (int, optional): The environment type
            console_logging (bool, optional): Whether to enable console logging
            
        Returns:
            bool: True if initialization was successful, False otherwise
        """
        
        import os
        logging_cache_directory = os.path.join(os.getcwd(), '.rapid-logging')
            
        os.makedirs(logging_cache_directory, exist_ok=True)
        
        app_id_bytes = app_id.encode('utf-8') if app_id else None
        package_name_bytes = package_name.encode('utf-8') if package_name else None
        platform_bytes = platform.encode('utf-8') if platform else None
        language_bytes = language.encode('utf-8') if language else None
        logging_dir_bytes = logging_cache_directory.encode('utf-8')
        
        result = lib.RAPID_Core_Initialize(
            app_id_bytes, 
            package_name_bytes, 
            platform_bytes, 
            language_bytes,
            environment,
            logging_dir_bytes,
            1 if console_logging else 0
        )
        
        return result != 0
    
    @staticmethod
    def version_name():
        """Get the RAPID Core version name"""
        version_ptr = lib.RAPID_Core_VersionName()
        if not version_ptr:
            return None
        return version_ptr.decode('utf-8')
    
    @staticmethod
    def build_id():
        """Get the RAPID Core build ID"""
        build_id_ptr = lib.RAPID_Core_BuildId()
        if not build_id_ptr:
            return None
        return build_id_ptr.decode('utf-8')
    
    @staticmethod
    def commit_hash():
        """Get the RAPID Core commit hash"""
        commit_hash_ptr = lib.RAPID_Core_CommitHash()
        if not commit_hash_ptr:
            return None
        return commit_hash_ptr.decode('utf-8') 