import ctypes
from ..lib import get_media_lib

lib = get_media_lib()

STATE_HANDLER_CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int)
PTS_UPDATE_CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_longlong)
UTS_UPDATE_CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_longlong)
RENDER_STATUS_CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int)

lib.RAPID_MediaPlayer_Create.argtypes = []
lib.RAPID_MediaPlayer_Create.restype = ctypes.c_void_p

lib.RAPID_MediaPlayer_Prepare.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.RAPID_MediaPlayer_Prepare.restype = None

lib.RAPID_MediaPlayer_Mute.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.RAPID_MediaPlayer_Mute.restype = None

lib.RAPID_MediaPlayer_IsMute.argtypes = [ctypes.c_void_p]
lib.RAPID_MediaPlayer_IsMute.restype = ctypes.c_int

lib.RAPID_MediaPlayer_Start.argtypes = [ctypes.c_void_p]
lib.RAPID_MediaPlayer_Start.restype = None

lib.RAPID_MediaPlayer_Pause.argtypes = [ctypes.c_void_p]
lib.RAPID_MediaPlayer_Pause.restype = None

lib.RAPID_MediaPlayer_Resume.argtypes = [ctypes.c_void_p]
lib.RAPID_MediaPlayer_Resume.restype = None

lib.RAPID_MediaPlayer_Stop.argtypes = [ctypes.c_void_p]
lib.RAPID_MediaPlayer_Stop.restype = None

lib.RAPID_MediaPlayer_State.argtypes = [ctypes.c_void_p]
lib.RAPID_MediaPlayer_State.restype = ctypes.c_int

lib.RAPID_MediaPlayer_Flush.argtypes = [ctypes.c_void_p]
lib.RAPID_MediaPlayer_Flush.restype = None

lib.RAPID_MediaPlayer_Destroy.argtypes = [ctypes.c_void_p]
lib.RAPID_MediaPlayer_Destroy.restype = None

lib.RAPID_MediaPlayer_BindPlayer.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.RAPID_MediaPlayer_BindPlayer.restype = None

lib.RAPID_MediaPlayer_SetVout.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.RAPID_MediaPlayer_SetVout.restype = None

lib.RAPID_MediaPlayer_SetAout.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.RAPID_MediaPlayer_SetAout.restype = None

lib.RAPID_MediaPlayer_Capture.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
lib.RAPID_MediaPlayer_Capture.restype = ctypes.c_int

lib.RAPID_MediaPlayer_StartRecord.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
lib.RAPID_MediaPlayer_StartRecord.restype = ctypes.c_int

lib.RAPID_MediaPlayer_StopRecord.argtypes = [ctypes.c_void_p]
lib.RAPID_MediaPlayer_StopRecord.restype = ctypes.c_int

lib.RAPID_MediaPlayer_EnableBuffering.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.RAPID_MediaPlayer_EnableBuffering.restype = None

lib.RAPID_MediaPlayer_EnableBufferingAutoAdaptive.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.RAPID_MediaPlayer_EnableBufferingAutoAdaptive.restype = None

lib.RAPID_MediaPlayer_EnableAout.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.RAPID_MediaPlayer_EnableAout.restype = None

lib.RAPID_MediaPlayer_GetPixelWidth.argtypes = [ctypes.c_void_p]
lib.RAPID_MediaPlayer_GetPixelWidth.restype = ctypes.c_int

lib.RAPID_MediaPlayer_GetPixelHeight.argtypes = [ctypes.c_void_p]
lib.RAPID_MediaPlayer_GetPixelHeight.restype = ctypes.c_int

lib.RAPID_MediaPlayer_GetUts.argtypes = [ctypes.c_void_p]
lib.RAPID_MediaPlayer_GetUts.restype = ctypes.c_longlong

lib.RAPID_MediaPlayer_GetPts.argtypes = [ctypes.c_void_p]
lib.RAPID_MediaPlayer_GetPts.restype = ctypes.c_longlong

lib.RAPID_MediaPlayer_SetPtsFunc.argtypes = [ctypes.c_void_p, PTS_UPDATE_CALLBACK]
lib.RAPID_MediaPlayer_SetPtsFunc.restype = None

lib.RAPID_MediaPlayer_SetUtsFunc.argtypes = [ctypes.c_void_p, UTS_UPDATE_CALLBACK]
lib.RAPID_MediaPlayer_SetUtsFunc.restype = None

lib.RAPID_MediaPlayer_SetRenderStateFunc.argtypes = [ctypes.c_void_p, RENDER_STATUS_CALLBACK]
lib.RAPID_MediaPlayer_SetRenderStateFunc.restype = None

lib.RAPID_MediaPlayer_SetRenderStatusSendPort.argtypes = [ctypes.c_void_p, ctypes.c_longlong]
lib.RAPID_MediaPlayer_SetRenderStatusSendPort.restype = None

class MediaPlayerState:
    IDLE = 0
    INITIALIZED = 1
    PREPARING = 2
    PREPARED = 3
    STARTED = 4
    PAUSED = 5
    STOPPED = 6
    COMPLETED = 7
    ERROR = 8

class MediaPlayer:
    def __init__(self):
        self._handle = lib.RAPID_MediaPlayer_Create()
        if not self._handle:
            raise RuntimeError("Failed to create media player")
        
        self._pts_callback = None
        self._uts_callback = None
        self._render_state_callback = None
    
    def __del__(self):
        self.destroy()
    
    def prepare(self, provider):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        if hasattr(provider, '_handle'):
            provider_handle = provider._handle
        else:
            provider_handle = provider
            
        lib.RAPID_MediaPlayer_Prepare(self._handle, provider_handle)
    
    def mute(self, mute=True):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        lib.RAPID_MediaPlayer_Mute(self._handle, 1 if mute else 0)
    
    def is_mute(self):
        if not self._handle:
            return False
        
        return lib.RAPID_MediaPlayer_IsMute(self._handle) != 0
    
    def start(self):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        lib.RAPID_MediaPlayer_Start(self._handle)
    
    def pause(self):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        lib.RAPID_MediaPlayer_Pause(self._handle)
    
    def resume(self):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        lib.RAPID_MediaPlayer_Resume(self._handle)
    
    def stop(self):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        lib.RAPID_MediaPlayer_Stop(self._handle)
    
    def get_state(self):
        if not self._handle:
            return MediaPlayerState.ERROR
        
        return lib.RAPID_MediaPlayer_State(self._handle)
    
    def flush(self):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        lib.RAPID_MediaPlayer_Flush(self._handle)
    
    def bind_player(self, main_player):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        if not main_player or not hasattr(main_player, '_handle'):
            raise ValueError("Invalid main player provided")
            
        lib.RAPID_MediaPlayer_BindPlayer(self._handle, main_player._handle)
    
    def set_vout(self, vout):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        lib.RAPID_MediaPlayer_SetVout(self._handle, vout)
    
    def set_aout(self, aout):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        lib.RAPID_MediaPlayer_SetAout(self._handle, aout)
    
    def capture(self, path):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        path_bytes = path.encode('utf-8') if path else None
        return lib.RAPID_MediaPlayer_Capture(self._handle, path_bytes) != 0
    
    def start_record(self, path):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        path_bytes = path.encode('utf-8') if path else None
        return lib.RAPID_MediaPlayer_StartRecord(self._handle, path_bytes) != 0
    
    def stop_record(self):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        return lib.RAPID_MediaPlayer_StopRecord(self._handle) != 0
    
    def enable_buffering(self, enable=True):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        lib.RAPID_MediaPlayer_EnableBuffering(self._handle, 1 if enable else 0)
    
    def enable_buffering_auto_adaptive(self, enable=True):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        lib.RAPID_MediaPlayer_EnableBufferingAutoAdaptive(self._handle, 1 if enable else 0)
    
    def enable_aout(self, enable=True):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        lib.RAPID_MediaPlayer_EnableAout(self._handle, 1 if enable else 0)
    
    def get_pixel_width(self):
        if not self._handle:
            return 0
        
        return lib.RAPID_MediaPlayer_GetPixelWidth(self._handle)
    
    def get_pixel_height(self):
        if not self._handle:
            return 0
        
        return lib.RAPID_MediaPlayer_GetPixelHeight(self._handle)
    
    def get_uts(self):
        if not self._handle:
            return 0
        
        return lib.RAPID_MediaPlayer_GetUts(self._handle)
    
    def get_pts(self):
        if not self._handle:
            return 0
        
        return lib.RAPID_MediaPlayer_GetPts(self._handle)
    
    def set_pts_callback(self, callback):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        @PTS_UPDATE_CALLBACK
        def pts_callback(pts):
            if callback:
                try:
                    callback(pts)
                except Exception as e:
                    print(f"Error in pts callback: {e}")
        
        self._pts_callback = pts_callback
        lib.RAPID_MediaPlayer_SetPtsFunc(self._handle, pts_callback)
    
    def set_uts_callback(self, callback):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        @UTS_UPDATE_CALLBACK
        def uts_callback(uts):
            if callback:
                try:
                    callback(uts)
                except Exception as e:
                    print(f"Error in uts callback: {e}")
        
        self._uts_callback = uts_callback
        lib.RAPID_MediaPlayer_SetUtsFunc(self._handle, uts_callback)
    
    def set_render_state_callback(self, callback):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        @RENDER_STATUS_CALLBACK
        def render_state_callback(state):
            if callback:
                try:
                    callback(state)
                except Exception as e:
                    print(f"Error in render state callback: {e}")
        
        self._render_state_callback = render_state_callback
        lib.RAPID_MediaPlayer_SetRenderStateFunc(self._handle, render_state_callback)
    
    def set_render_status_send_port(self, port):
        if not self._handle:
            raise RuntimeError("Media player has been destroyed")
        
        lib.RAPID_MediaPlayer_SetRenderStatusSendPort(self._handle, port)
    
    def destroy(self):
        if self._handle:
            lib.RAPID_MediaPlayer_Destroy(self._handle)
            self._handle = None
            self._pts_callback = None
            self._uts_callback = None
            self._render_state_callback = None 