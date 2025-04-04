#!/usr/bin/env python3
"""
RAPID Media SDK Basic Example
"""

import os
import sys
import time

# Add parent directory to module search path to import rapid_kit module
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from rapid_kit import Core, MediaPlayer, MediaChat, RGBFormat, set_rgb_pixel_format
from rapid_kit.core import PipeProxy, LiveStream

def main():
    # Print useful path information
    print(f"Script directory: {os.path.dirname(os.path.abspath(__file__))}")
    print(f"Current working directory: {os.getcwd()}")
    
    # View all loaded libraries
    from rapid_kit.lib import get_all_loaded_libs
    all_libs = get_all_loaded_libs()
    if all_libs:
        print(f"Loaded {len(all_libs)} dynamic libraries:")
        for lib_name in all_libs:
            print(f"  - {lib_name}")
    else:
        print("No additional libraries loaded")
    
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
        
        # Create a media player and prepare it with the stream provider
        player = MediaPlayer()
        provider = stream.get_provider()
        player.prepare(provider)
        
        # Set callbacks for media events
        def on_pts_update(pts):
            print(f"PTS updated: {pts}")
        
        def on_uts_update(uts):
            print(f"UTS updated: {uts}")
        
        def on_render_state(state):
            print(f"Render state changed: {state}")
        
        player.set_pts_callback(on_pts_update)
        player.set_uts_callback(on_uts_update)
        player.set_render_state_callback(on_render_state)
        
        # Start the player
        player.start()
        print("Media player started")
        
        # Let it run for a while
        print("Playing for 10 seconds...")
        time.sleep(10)
        
        # Check current dimensions
        width = player.get_pixel_width()
        height = player.get_pixel_height()
        print(f"Video dimensions: {width}x{height}")
        
        # Capture a screenshot
        screenshot_path = "screenshot.jpg"
        if player.capture(screenshot_path):
            print(f"Screenshot saved to {screenshot_path}")
        else:
            print("Failed to capture screenshot")
        
        # Stop the player
        player.stop()
        print("Media player stopped")
        
        # Create a media chat instance
        chat = MediaChat()
        chat.set_chat_channel(pipe)
        chat.start()
        print("Media chat started")
        
        # Let it run for a while
        print("Chat active for 5 seconds...")
        time.sleep(5)
        
        # Stop the chat
        chat.stop()
        print("Media chat stopped")
        
        # Release resources
        chat.release()
        player.destroy()
        stream.stop()
        stream.release()
        
    except Exception as e:
        print(f"Error during media operations: {e}")
    
    # Clean up
    pipe.abolish()
    pipe.destroy()
    print("Resources cleaned up")

if __name__ == "__main__":
    main() 