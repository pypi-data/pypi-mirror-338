import ctypes
import json
from ..lib import get_lib

lib = get_lib()

# Define function prototypes
lib.RAPID_Core_LocalNetwork_SetBroadcastAddress.argtypes = [ctypes.c_char_p]
lib.RAPID_Core_LocalNetwork_SetBroadcastAddress.restype = None

lib.RAPID_Core_LanScanner_Create.argtypes = []
lib.RAPID_Core_LanScanner_Create.restype = ctypes.c_void_p

lib.RAPID_Core_LanScanner_Destroy.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LanScanner_Destroy.restype = None

lib.RAPID_Core_LanScanner_FoundDevices.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LanScanner_FoundDevices.restype = ctypes.c_char_p

lib.RAPID_Core_LanScanner_Start.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LanScanner_Start.restype = None

lib.RAPID_Core_LanScanner_Stop.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LanScanner_Stop.restype = None

def set_broadcast_address(address):
    """
    Set the broadcast address for local network scanning.
    
    Args:
        address (str): The broadcast address to use
    """
    if not address:
        return
    
    address_bytes = address.encode('utf-8')
    lib.RAPID_Core_LocalNetwork_SetBroadcastAddress(address_bytes)

class LanScanner:
    def __init__(self):
        """Initialize a LAN scanner to discover devices on the local network"""
        self._handle = lib.RAPID_Core_LanScanner_Create()
        if not self._handle:
            raise RuntimeError("Failed to create LAN scanner")
    
    def __del__(self):
        """Clean up resources when object is destroyed"""
        self.destroy()
    
    def start(self):
        """Start scanning for devices on the local network"""
        if not self._handle:
            raise RuntimeError("LAN scanner has been destroyed")
        
        lib.RAPID_Core_LanScanner_Start(self._handle)
    
    def stop(self):
        """Stop scanning for devices"""
        if not self._handle:
            raise RuntimeError("LAN scanner has been destroyed")
        
        lib.RAPID_Core_LanScanner_Stop(self._handle)
    
    def get_found_devices(self):
        """
        Get the list of devices found on the local network.
        
        Returns:
            list: List of discovered devices
        """
        if not self._handle:
            raise RuntimeError("LAN scanner has been destroyed")
        
        devices_ptr = lib.RAPID_Core_LanScanner_FoundDevices(self._handle)
        if not devices_ptr:
            return []
        
        devices_json = devices_ptr.decode('utf-8')
        try:
            return json.loads(devices_json)
        except json.JSONDecodeError:
            return []
    
    def destroy(self):
        """Release the LAN scanner resources"""
        if self._handle:
            lib.RAPID_Core_LanScanner_Destroy(self._handle)
            self._handle = None 