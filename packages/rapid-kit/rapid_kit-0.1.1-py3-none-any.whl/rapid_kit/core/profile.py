import ctypes
from ..lib import get_lib

lib = get_lib()

class BindingProfileByteArray(ctypes.Structure):
    _fields_ = [
        ("data", ctypes.c_char_p),
        ("length", ctypes.c_int)
    ]

# Define function prototypes
lib.RAPID_Core_BindingProfile_Create.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
lib.RAPID_Core_BindingProfile_Create.restype = ctypes.c_char_p

lib.RAPID_Core_BindingProfileWithHeader.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
lib.RAPID_Core_BindingProfileWithHeader.restype = ctypes.POINTER(BindingProfileByteArray)

lib.RAPID_Core_BindingProfile_Release.argtypes = [ctypes.c_char_p]
lib.RAPID_Core_BindingProfile_Release.restype = None

lib.RAPID_Core_BindingProfile_ByteArray_Release.argtypes = [ctypes.POINTER(BindingProfileByteArray)]
lib.RAPID_Core_BindingProfile_ByteArray_Release.restype = None

class BindingProfile:
    @staticmethod
    def create(wifi, password, bind_token):
        """
        Create a binding profile.
        
        Args:
            wifi (str): The WiFi SSID
            password (str): The WiFi password
            bind_token (str): The binding token
            
        Returns:
            str: The created binding profile
        """
        wifi_bytes = wifi.encode('utf-8') if wifi else None
        pwd_bytes = password.encode('utf-8') if password else None
        token_bytes = bind_token.encode('utf-8') if bind_token else None
        
        profile_ptr = lib.RAPID_Core_BindingProfile_Create(wifi_bytes, pwd_bytes, token_bytes)
        if not profile_ptr:
            return None
        
        profile = profile_ptr.decode('utf-8')
        lib.RAPID_Core_BindingProfile_Release(profile_ptr)
        return profile
    
    @staticmethod
    def create_with_header(wifi, password, bind_token):
        """
        Create a binding profile with header.
        
        Args:
            wifi (str): The WiFi SSID
            password (str): The WiFi password
            bind_token (str): The binding token
            
        Returns:
            bytes: The binding profile bytes with header
        """
        wifi_bytes = wifi.encode('utf-8') if wifi else None
        pwd_bytes = password.encode('utf-8') if password else None
        token_bytes = bind_token.encode('utf-8') if bind_token else None
        
        byte_array_ptr = lib.RAPID_Core_BindingProfileWithHeader(wifi_bytes, pwd_bytes, token_bytes)
        if not byte_array_ptr:
            return None
        
        byte_array = byte_array_ptr.contents
        if not byte_array.data or byte_array.length <= 0:
            lib.RAPID_Core_BindingProfile_ByteArray_Release(byte_array_ptr)
            return None
        
        # Copy the data to a Python bytes object
        result = bytes(byte_array.data[:byte_array.length])
        lib.RAPID_Core_BindingProfile_ByteArray_Release(byte_array_ptr)
        return result 