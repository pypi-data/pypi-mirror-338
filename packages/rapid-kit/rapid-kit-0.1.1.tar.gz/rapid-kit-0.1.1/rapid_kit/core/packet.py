import ctypes
from enum import IntEnum
from ..lib import get_lib

lib = get_lib()

class StreamCodecID(IntEnum):
    UNKNOWN = 0x00
    AVC = 0x4E
    HEVC = 0x50
    MJPEG = 0x4F
    G711A = 0x8A
    
    END = 0x100
    SPEED = 0x102
    SPECIAL = 0x200

class StreamPacket(ctypes.Structure):
    _fields_ = [
        ("buffer", ctypes.c_char_p),
        ("codec_id", ctypes.c_int32),
        ("sub_type", ctypes.c_int32),
        ("frame_type", ctypes.c_int32),
        ("buffer_size", ctypes.c_int32),
        ("seq_no", ctypes.c_int32),
        ("ts", ctypes.c_int64),
        ("utc_ts", ctypes.c_int64),
        ("final_packet", ctypes.c_int8),
        ("speed_packet", ctypes.c_int8),
        ("speed", ctypes.c_int8)
    ]

# Define function prototypes
lib.RAPID_Core_StreamPacket_Create_From_Buffer.argtypes = [ctypes.c_char_p, ctypes.c_int32]
lib.RAPID_Core_StreamPacket_Create_From_Buffer.restype = ctypes.POINTER(StreamPacket)

lib.RAPID_Core_StreamPacket_Create.argtypes = []
lib.RAPID_Core_StreamPacket_Create.restype = ctypes.POINTER(StreamPacket)

lib.RAPID_Core_StreamPacket_Free.argtypes = [ctypes.POINTER(StreamPacket)]
lib.RAPID_Core_StreamPacket_Free.restype = None

lib.RAPID_Core_StreamPacket_Fill.argtypes = [ctypes.POINTER(StreamPacket), ctypes.c_char_p, ctypes.c_int32]
lib.RAPID_Core_StreamPacket_Fill.restype = None

def create_stream_packet(buffer=None, buffer_size=None):
    """
    Create a stream packet, optionally with the given buffer.
    
    Args:
        buffer (bytes, optional): The packet buffer data
        buffer_size (int, optional): The size of the buffer
        
    Returns:
        StreamPacket: A new stream packet object
    """
    if buffer:
        if not buffer_size:
            buffer_size = len(buffer)
        
        return lib.RAPID_Core_StreamPacket_Create_From_Buffer(buffer, buffer_size).contents
    else:
        return lib.RAPID_Core_StreamPacket_Create().contents

def free_stream_packet(packet):
    """
    Free a stream packet.
    
    Args:
        packet (StreamPacket): The packet to free
    """
    if isinstance(packet, StreamPacket):
        # Convert to pointer
        packet_ptr = ctypes.pointer(packet)
        lib.RAPID_Core_StreamPacket_Free(packet_ptr)

def fill_stream_packet(packet, buffer, buffer_size=None):
    """
    Fill a stream packet with the given buffer.
    
    Args:
        packet (StreamPacket): The packet to fill
        buffer (bytes): The buffer data
        buffer_size (int, optional): The size of the buffer
    """
    if not isinstance(packet, StreamPacket):
        raise TypeError("packet must be a StreamPacket instance")
    
    if not buffer_size:
        buffer_size = len(buffer)
    
    # Convert to pointer
    packet_ptr = ctypes.pointer(packet)
    lib.RAPID_Core_StreamPacket_Fill(packet_ptr, buffer, buffer_size) 