# RAPID Kit

Python SDK for the RAPID Core, Media and SDL libraries.

## Installation

```bash
pip install rapid-kit
```

## Quick Start

```python
from rapid_kit import Core

# Initialize the library
Core.initialize(
    app_id="your_app_id",
    package_name="com.example.rapid",
    environment=Core.ENV_DEVELOPMENT
)

# Use Media Player
from rapid_kit import MediaPlayer, RGBFormat, set_rgb_pixel_format

# Set RGB format for rendering
set_rgb_pixel_format(RGBFormat.RGBA)

# Create audio/video devices
from rapid_kit import create_silence_vout, create_aout_for_audio_queue

audio_out = create_aout_for_audio_queue()
video_out = create_silence_vout()

# Use with media player
player = MediaPlayer()
player.set_vout(video_out)
player.set_aout(audio_out)
```

## Features

- **Core API**: Authentication, device communication, live streaming
- **Media API**: Video playback, recording, and capture
- **SDL API**: Audio/video device integration

## Requirements

- Python 3.6+
- Internet connection for automatic library download (first run only)

## License

MIT License 