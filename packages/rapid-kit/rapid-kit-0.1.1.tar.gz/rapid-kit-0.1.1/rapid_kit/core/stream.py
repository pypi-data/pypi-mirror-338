import ctypes
from ..lib import get_lib
from .packet import StreamPacket, StreamCodecID

lib = get_lib()

# Define function prototypes for LiveStream
lib.RAPID_Core_LiveStream_CreateDefault.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LiveStream_CreateDefault.restype = ctypes.c_void_p

lib.RAPID_Core_LiveStream_CreateSecondary.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LiveStream_CreateSecondary.restype = ctypes.c_void_p

lib.RAPID_Core_LiveStream_Start.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LiveStream_Start.restype = None

lib.RAPID_Core_LiveStream_Stop.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LiveStream_Stop.restype = None

lib.RAPID_Core_LiveStream_IsStarted.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LiveStream_IsStarted.restype = ctypes.c_int

lib.RAPID_Core_LiveStream_SwitchQuality.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.RAPID_Core_LiveStream_SwitchQuality.restype = None

lib.RAPID_Core_LiveStream_RequestKeyFrame.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LiveStream_RequestKeyFrame.restype = None

lib.RAPID_Core_LiveStream_Release.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LiveStream_Release.restype = None

lib.RAPID_Core_LiveStream_IndexedProvider.argtypes = [ctypes.c_void_p, ctypes.c_uint]
lib.RAPID_Core_LiveStream_IndexedProvider.restype = ctypes.c_void_p

# Define function prototypes for LocalReplayStream
lib.RAPID_Core_LocalReplayStream_Create.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LocalReplayStream_Create.restype = ctypes.c_void_p

lib.RAPID_Core_LocalReplayStream_Prepare.argtypes = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint]
lib.RAPID_Core_LocalReplayStream_Prepare.restype = None

lib.RAPID_Core_LocalReplayStream_Start.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LocalReplayStream_Start.restype = None

lib.RAPID_Core_LocalReplayStream_Stop.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LocalReplayStream_Stop.restype = None

lib.RAPID_Core_LocalReplayStream_IsStarted.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LocalReplayStream_IsStarted.restype = ctypes.c_int

lib.RAPID_Core_LocalReplayStream_Seek.argtypes = [ctypes.c_void_p, ctypes.c_longlong]
lib.RAPID_Core_LocalReplayStream_Seek.restype = None

lib.RAPID_Core_LocalReplayStream_SetSpeed.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.RAPID_Core_LocalReplayStream_SetSpeed.restype = None

lib.RAPID_Core_LocalReplayStream_Pause.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LocalReplayStream_Pause.restype = None

lib.RAPID_Core_LocalReplayStream_IsPaused.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LocalReplayStream_IsPaused.restype = ctypes.c_int

lib.RAPID_Core_LocalReplayStream_Resume.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LocalReplayStream_Resume.restype = None

lib.RAPID_Core_LocalReplayStream_Release.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_LocalReplayStream_Release.restype = None

lib.RAPID_Core_LocalReplayStream_IndexedProvider.argtypes = [ctypes.c_void_p, ctypes.c_uint]
lib.RAPID_Core_LocalReplayStream_IndexedProvider.restype = ctypes.c_void_p

# Define function prototypes for CloudReplayStream
lib.RAPID_Core_CloudReplayStream_Create.argtypes = [ctypes.c_char_p]
lib.RAPID_Core_CloudReplayStream_Create.restype = ctypes.c_void_p

lib.RAPID_Core_CloudReplayStream_Prepare.argtypes = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_char_p]
lib.RAPID_Core_CloudReplayStream_Prepare.restype = None

lib.RAPID_Core_CloudReplayStream_Start.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_CloudReplayStream_Start.restype = None

lib.RAPID_Core_CloudReplayStream_Seek.argtypes = [ctypes.c_void_p, ctypes.c_uint]
lib.RAPID_Core_CloudReplayStream_Seek.restype = None

lib.RAPID_Core_CloudReplayStream_SetSpeed.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.RAPID_Core_CloudReplayStream_SetSpeed.restype = None

lib.RAPID_Core_CloudReplayStream_Pause.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_CloudReplayStream_Pause.restype = None

lib.RAPID_Core_CloudReplayStream_Resume.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_CloudReplayStream_Resume.restype = None

lib.RAPID_Core_CloudReplayStream_Stop.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_CloudReplayStream_Stop.restype = None

lib.RAPID_Core_CloudReplayStream_IsPaused.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_CloudReplayStream_IsPaused.restype = ctypes.c_int

lib.RAPID_Core_CloudReplayStream_IsStarted.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_CloudReplayStream_IsStarted.restype = ctypes.c_int

lib.RAPID_Core_CloudReplayStream_Release.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_CloudReplayStream_Release.restype = None

lib.RAPID_Core_CloudReplayStream_SetFileNotFoundSendPort.argtypes = [ctypes.c_void_p, ctypes.c_longlong]
lib.RAPID_Core_CloudReplayStream_SetFileNotFoundSendPort.restype = None

lib.RAPID_Core_CloudReplayStream_SetDownloadCompleteSendPort.argtypes = [ctypes.c_void_p, ctypes.c_longlong]
lib.RAPID_Core_CloudReplayStream_SetDownloadCompleteSendPort.restype = None

lib.RAPID_Core_CloudReplayStream_IndexedProvider.argtypes = [ctypes.c_void_p, ctypes.c_uint]
lib.RAPID_Core_CloudReplayStream_IndexedProvider.restype = ctypes.c_void_p

# Define function prototypes for RelayStream
lib.RAPID_Core_RelayStream_Create.argtypes = [ctypes.c_char_p]
lib.RAPID_Core_RelayStream_Create.restype = ctypes.c_void_p

lib.RAPID_Core_RelayStream_Enqueue.argtypes = [ctypes.c_void_p, ctypes.POINTER(StreamPacket)]
lib.RAPID_Core_RelayStream_Enqueue.restype = None

lib.RAPID_Core_RelayStream_Release.argtypes = [ctypes.c_void_p]
lib.RAPID_Core_RelayStream_Release.restype = None

lib.RAPID_Core_RelayStream_IndexedProvider.argtypes = [ctypes.c_void_p, ctypes.c_uint]
lib.RAPID_Core_RelayStream_IndexedProvider.restype = ctypes.c_void_p

class LiveStream:
    def __init__(self, pipe_proxy, secondary=False):
        """
        Initialize a live stream with the given pipe proxy.
        
        Args:
            pipe_proxy: The pipe proxy object to use for the stream
            secondary (bool): Whether to create a secondary stream
        """
        if not pipe_proxy or not hasattr(pipe_proxy, '_handle'):
            raise ValueError("Invalid pipe_proxy provided")
        
        if secondary:
            self._handle = lib.RAPID_Core_LiveStream_CreateSecondary(pipe_proxy._handle)
        else:
            self._handle = lib.RAPID_Core_LiveStream_CreateDefault(pipe_proxy._handle)
        
        if not self._handle:
            raise RuntimeError("Failed to create live stream")
    
    def __del__(self):
        """Clean up resources when object is destroyed"""
        self.release()
    
    def start(self):
        """Start the live stream"""
        if not self._handle:
            raise RuntimeError("Live stream has been released")
        
        lib.RAPID_Core_LiveStream_Start(self._handle)
    
    def stop(self):
        """Stop the live stream"""
        if not self._handle:
            raise RuntimeError("Live stream has been released")
        
        lib.RAPID_Core_LiveStream_Stop(self._handle)
    
    def is_started(self):
        """
        Check if the live stream is started.
        
        Returns:
            bool: True if the stream is started, False otherwise
        """
        if not self._handle:
            return False
        
        return lib.RAPID_Core_LiveStream_IsStarted(self._handle) != 0
    
    def switch_quality(self, quality):
        """
        Switch the stream quality.
        
        Args:
            quality (int): The quality level to switch to
        """
        if not self._handle:
            raise RuntimeError("Live stream has been released")
        
        lib.RAPID_Core_LiveStream_SwitchQuality(self._handle, quality)
    
    def request_key_frame(self):
        """Request a key frame from the stream"""
        if not self._handle:
            raise RuntimeError("Live stream has been released")
        
        lib.RAPID_Core_LiveStream_RequestKeyFrame(self._handle)
    
    def get_provider(self, index=0):
        """
        Get a stream provider for the given index.
        
        Args:
            index (int): The provider index
            
        Returns:
            int: The provider handle
        """
        if not self._handle:
            raise RuntimeError("Live stream has been released")
        
        return lib.RAPID_Core_LiveStream_IndexedProvider(self._handle, index)
    
    def release(self):
        """Release the live stream resources"""
        if self._handle:
            lib.RAPID_Core_LiveStream_Release(self._handle)
            self._handle = None

class LocalReplayStream:
    def __init__(self, pipe_proxy):
        """
        Initialize a local replay stream with the given pipe proxy.
        
        Args:
            pipe_proxy: The pipe proxy object to use for the stream
        """
        if not pipe_proxy or not hasattr(pipe_proxy, '_handle'):
            raise ValueError("Invalid pipe_proxy provided")
        
        self._handle = lib.RAPID_Core_LocalReplayStream_Create(pipe_proxy._handle)
        if not self._handle:
            raise RuntimeError("Failed to create local replay stream")
    
    def __del__(self):
        """Clean up resources when object is destroyed"""
        self.release()
    
    def prepare(self, start_timestamp_s, end_timestamp_s):
        """
        Prepare the replay stream with the specified time range.
        
        Args:
            start_timestamp_s (int): Start time in seconds
            end_timestamp_s (int): End time in seconds
        """
        if not self._handle:
            raise RuntimeError("Local replay stream has been released")
        
        lib.RAPID_Core_LocalReplayStream_Prepare(self._handle, start_timestamp_s, end_timestamp_s)
    
    def start(self):
        """Start the replay stream"""
        if not self._handle:
            raise RuntimeError("Local replay stream has been released")
        
        lib.RAPID_Core_LocalReplayStream_Start(self._handle)
    
    def stop(self):
        """Stop the replay stream"""
        if not self._handle:
            raise RuntimeError("Local replay stream has been released")
        
        lib.RAPID_Core_LocalReplayStream_Stop(self._handle)
    
    def is_started(self):
        """
        Check if the replay stream is started.
        
        Returns:
            bool: True if the stream is started, False otherwise
        """
        if not self._handle:
            return False
        
        return lib.RAPID_Core_LocalReplayStream_IsStarted(self._handle) != 0
    
    def seek(self, timestamp):
        """
        Seek to a specific timestamp in the replay.
        
        Args:
            timestamp (int): The timestamp to seek to
        """
        if not self._handle:
            raise RuntimeError("Local replay stream has been released")
        
        lib.RAPID_Core_LocalReplayStream_Seek(self._handle, timestamp)
    
    def set_speed(self, speed):
        """
        Set the playback speed.
        
        Args:
            speed (int): The playback speed multiplier
        """
        if not self._handle:
            raise RuntimeError("Local replay stream has been released")
        
        lib.RAPID_Core_LocalReplayStream_SetSpeed(self._handle, speed)
    
    def pause(self):
        """Pause the replay playback"""
        if not self._handle:
            raise RuntimeError("Local replay stream has been released")
        
        lib.RAPID_Core_LocalReplayStream_Pause(self._handle)
    
    def is_paused(self):
        """
        Check if the replay is paused.
        
        Returns:
            bool: True if paused, False otherwise
        """
        if not self._handle:
            return False
        
        return lib.RAPID_Core_LocalReplayStream_IsPaused(self._handle) != 0
    
    def resume(self):
        """Resume the replay playback"""
        if not self._handle:
            raise RuntimeError("Local replay stream has been released")
        
        lib.RAPID_Core_LocalReplayStream_Resume(self._handle)
    
    def get_provider(self, index=0):
        """
        Get a stream provider for the given index.
        
        Args:
            index (int): The provider index
            
        Returns:
            int: The provider handle
        """
        if not self._handle:
            raise RuntimeError("Local replay stream has been released")
        
        return lib.RAPID_Core_LocalReplayStream_IndexedProvider(self._handle, index)
    
    def release(self):
        """Release the replay stream resources"""
        if self._handle:
            lib.RAPID_Core_LocalReplayStream_Release(self._handle)
            self._handle = None

class CloudReplayStream:
    def __init__(self, device_id):
        """
        Initialize a cloud replay stream for the specified device.
        
        Args:
            device_id (str): The ID of the device to replay from
        """
        device_id_bytes = device_id.encode('utf-8') if device_id else None
        self._handle = lib.RAPID_Core_CloudReplayStream_Create(device_id_bytes)
        if not self._handle:
            raise RuntimeError("Failed to create cloud replay stream")
    
    def __del__(self):
        """Clean up resources when object is destroyed"""
        self.release()
    
    def prepare(self, start_timestamp_s, end_timestamp_s, storage_id):
        """
        Prepare the replay stream with the specified time range and storage ID.
        
        Args:
            start_timestamp_s (int): Start time in seconds
            end_timestamp_s (int): End time in seconds
            storage_id (str): The storage ID
        """
        if not self._handle:
            raise RuntimeError("Cloud replay stream has been released")
        
        storage_id_bytes = storage_id.encode('utf-8') if storage_id else None
        lib.RAPID_Core_CloudReplayStream_Prepare(
            self._handle, start_timestamp_s, end_timestamp_s, storage_id_bytes
        )
    
    def start(self):
        """Start the replay stream"""
        if not self._handle:
            raise RuntimeError("Cloud replay stream has been released")
        
        lib.RAPID_Core_CloudReplayStream_Start(self._handle)
    
    def seek(self, timestamp_s):
        """
        Seek to a specific timestamp in the replay.
        
        Args:
            timestamp_s (int): The timestamp in seconds to seek to
        """
        if not self._handle:
            raise RuntimeError("Cloud replay stream has been released")
        
        lib.RAPID_Core_CloudReplayStream_Seek(self._handle, timestamp_s)
    
    def set_speed(self, speed):
        """
        Set the playback speed.
        
        Args:
            speed (int): The playback speed multiplier
        """
        if not self._handle:
            raise RuntimeError("Cloud replay stream has been released")
        
        lib.RAPID_Core_CloudReplayStream_SetSpeed(self._handle, speed)
    
    def pause(self):
        """Pause the replay playback"""
        if not self._handle:
            raise RuntimeError("Cloud replay stream has been released")
        
        lib.RAPID_Core_CloudReplayStream_Pause(self._handle)
    
    def resume(self):
        """Resume the replay playback"""
        if not self._handle:
            raise RuntimeError("Cloud replay stream has been released")
        
        lib.RAPID_Core_CloudReplayStream_Resume(self._handle)
    
    def stop(self):
        """Stop the replay stream"""
        if not self._handle:
            raise RuntimeError("Cloud replay stream has been released")
        
        lib.RAPID_Core_CloudReplayStream_Stop(self._handle)
    
    def is_paused(self):
        """
        Check if the replay is paused.
        
        Returns:
            bool: True if paused, False otherwise
        """
        if not self._handle:
            return False
        
        return lib.RAPID_Core_CloudReplayStream_IsPaused(self._handle) != 0
    
    def is_started(self):
        """
        Check if the replay stream is started.
        
        Returns:
            bool: True if the stream is started, False otherwise
        """
        if not self._handle:
            return False
        
        return lib.RAPID_Core_CloudReplayStream_IsStarted(self._handle) != 0
    
    def set_file_not_found_send_port(self, port):
        """
        Set the port for file not found notifications.
        
        Args:
            port (int): The port number
        """
        if not self._handle:
            raise RuntimeError("Cloud replay stream has been released")
        
        lib.RAPID_Core_CloudReplayStream_SetFileNotFoundSendPort(self._handle, port)
    
    def set_download_complete_send_port(self, port):
        """
        Set the port for download complete notifications.
        
        Args:
            port (int): The port number
        """
        if not self._handle:
            raise RuntimeError("Cloud replay stream has been released")
        
        lib.RAPID_Core_CloudReplayStream_SetDownloadCompleteSendPort(self._handle, port)
    
    def get_provider(self, index=0):
        """
        Get a stream provider for the given index.
        
        Args:
            index (int): The provider index
            
        Returns:
            int: The provider handle
        """
        if not self._handle:
            raise RuntimeError("Cloud replay stream has been released")
        
        return lib.RAPID_Core_CloudReplayStream_IndexedProvider(self._handle, index)
    
    def release(self):
        """Release the replay stream resources"""
        if self._handle:
            lib.RAPID_Core_CloudReplayStream_Release(self._handle)
            self._handle = None

class RelayStream:
    def __init__(self, device_id):
        """
        Initialize a relay stream for the specified device.
        
        Args:
            device_id (str): The ID of the device to relay to
        """
        device_id_bytes = device_id.encode('utf-8') if device_id else None
        self._handle = lib.RAPID_Core_RelayStream_Create(device_id_bytes)
        if not self._handle:
            raise RuntimeError("Failed to create relay stream")
    
    def __del__(self):
        """Clean up resources when object is destroyed"""
        self.release()
    
    def enqueue(self, packet):
        """
        Enqueue a packet for relay.
        
        Args:
            packet (StreamPacket): The packet to enqueue
        """
        if not self._handle:
            raise RuntimeError("Relay stream has been released")
        
        if not isinstance(packet, StreamPacket):
            raise TypeError("packet must be a StreamPacket instance")
        
        lib.RAPID_Core_RelayStream_Enqueue(self._handle, ctypes.byref(packet))
    
    def get_provider(self, index=0):
        """
        Get a stream provider for the given index.
        
        Args:
            index (int): The provider index
            
        Returns:
            int: The provider handle
        """
        if not self._handle:
            raise RuntimeError("Relay stream has been released")
        
        return lib.RAPID_Core_RelayStream_IndexedProvider(self._handle, index)
    
    def release(self):
        """Release the relay stream resources"""
        if self._handle:
            lib.RAPID_Core_RelayStream_Release(self._handle)
            self._handle = None 