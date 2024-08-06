# 360 Video Timestamp Adder

A Python script that adds timestamps to video files, particularly useful for analyzing specific parts of cropped views of 360 videos at an angle.

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Copying File Path](#copying-file-path)
   - [Running the Script](#running-the-script)
4. [Important Notice](#important-notice)
5. [Troubleshooting](#troubleshooting)

## Requirements

- Python 3.6+
- `moviepy` library
- `ffmpeg`
- `ImageMagick`

## Installation

First-time setup:

1. Open Terminal
2. Navigate to the project directory:

`cd /path/to/project`

3. Create and activate a virtual environment:

```python3 -m venv venv
   source venv/bin/activate
```

4. Install required packages:

```
pip install moviepy ffmpeg ffmpeg-python
brew install imagemagick
pip install .
```

## Usage

### Copying File Path

1. In Finder, press `Cmd-Option-P` to show the file path at the bottom
2. Right-click on the file name in the filepath
3. Choose "Copy {filename} as Pathname"

### Running the Script

1. Open Terminal
2. Run the command:

```
add-timestamp "/path/to/your/video.mp4" [--start_time "MM:SS"]
```

Replace `/path/to/your/video.mp4` with your video's file path
Optionally, add `--start_time MM:SS` to specify a start time

The processed video will be saved in the same directory as the original, with "\_output" added to the filename.

## Important Notice

Always change to the project directory before running commands:

```
cd /path/to/video_timestamps/video_timestamps
```

The first video_timestamps is the repository name, and the second is folder with two file: `__init__.py` and `add_timestamp.py``. This ensures that the script uses the correct relative paths and doesn't interfere with other projects.

## Troubleshooting

If you encounter issues:

1. Ensure all requirements are installed
2. Check that you're in the correct directory
3. Verify the file path is correct
4. Make sure the virtual environment is activated

For further assistance, please open an issue on GitHub.
