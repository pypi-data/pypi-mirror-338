#!/usr/bin/env python3
"""
RAPID SDL Example

This example demonstrates how to use SDL audio and video components
with the RAPID Media Player.
"""

import os
import sys
import time

# Add parent directory to module search path to import rapid_kit module
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from rapid_kit import (
    Core, MediaPlayer, RGBFormat, set_rgb_pixel_format,
    create_aout_for_audio_queue, create_silence_vout, create_silence_aout,
    create_vout_simple_callback, VoutFrameCallback
)
from rapid_kit.core import PipeProxy, LiveStream

def main():
    # Print useful path information
    print(f"Script directory: {os.path.dirname(os.path.abspath(__file__))}")
    print(f"Current working directory: {os.getcwd()}")
    
    # Initialize RAPID Core library
    success = Core.initialize(
        app_id="com.example.rapid",
        package_name="com.example.rapid.demo",
        environment=Core.ENV_DEVELOPMENT,
        console_logging=True
    )
    
    if not success:
        print("Failed to initialize RAPID Core")
        return
    
    # Set RGB pixel format
    set_rgb_pixel_format(RGBFormat.RGBA)
    print("Set RGB pixel format to RGBA")
    
    # Connect to a device
    device_id = "device_123"  # Replace with actual device ID
    pipe = PipeProxy(device_id)
    
    # Set up a status callback
    def on_status_change(status):
        print(f"Pipe status changed: {status}")
    
    pipe.set_status_callback(on_status_change)
    
    # Establish connection
    pipe.establish()
    
    # Wait for connection to establish
    print("Establishing connection...")
    for _ in range(10):
        time.sleep(0.5)
        status = pipe.get_status()
        if status == 2:  # Connected (check actual status codes)
            print("Connection established!")
            break
    else:
        print("Failed to establish connection")
        pipe.destroy()
        return
    
    # Create and start a live stream
    try:
        stream = LiveStream(pipe)
        stream.start()
        print("Stream started")
        
        # Create audio outputs
        audio_queue_out = create_aout_for_audio_queue()
        print("Created AudioQueue output device")
        
        silence_vout = create_silence_vout()
        print("Created silent video output device")
        
        silence_aout = create_silence_aout()
        print("Created silent audio output device")
        
        # Create a frame callback
        frame_count = 0
        
        @VoutFrameCallback
        def frame_callback(overlay, user_data):
            nonlocal frame_count
            frame_count += 1
            if frame_count % 30 == 0:  # Log every 30 frames
                print(f"Received frame #{frame_count}")
        
        callback_vout = create_vout_simple_callback(frame_callback)
        print("Created video output with callback")
        
        # Create a media player and prepare it with the stream provider
        player = MediaPlayer()
        provider = stream.get_provider()
        player.prepare(provider)
        
        # Set video and audio outputs
        player.set_vout(callback_vout)
        player.set_aout(audio_queue_out)
        
        # Start the player
        player.start()
        print("Media player started with SDL outputs")
        
        # Let it run for a while
        print("Playing for 10 seconds...")
        time.sleep(10)
        
        # Switch to silent devices
        player.stop()
        player.set_vout(silence_vout)
        player.set_aout(silence_aout)
        player.start()
        print("Switched to silent devices")
        
        # Let it run a bit longer
        print("Playing with silent devices for 5 seconds...")
        time.sleep(5)
        
        # Stop the player
        player.stop()
        print("Media player stopped")
        
        # Release resources
        player.destroy()
        stream.stop()
        stream.release()
        
    except Exception as e:
        print(f"Error during SDL operations: {e}")
    
    # Clean up
    pipe.abolish()
    pipe.destroy()
    print("Resources cleaned up")

if __name__ == "__main__":
    main() 