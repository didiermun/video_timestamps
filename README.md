# 360 Video Timestamp Adder

This repository contains a Python script that adds timestamps to video files using the `moviepy` library. This is particularly useful for analyzing specific parts of cropped view of your 360 videos at an angle, where you can easily reference the time information embedded in the video itself.

## Requirements

- Python 3.6+
- `moviepy` library
- `ffmpeg`
- `ImageMagick`

# Usage

## Copying file path

If you can't see file path of your current location at the bottom of Finder, click Cmd-Option-P

- Click on file you wish to copy path of
- Right click on the file name in the filepath at the bottom of your Finder, and choose "Copy {filename} as Pathname"

You've got your file path!!

## Important Notice

To run terminal commands, change the directory to the folder where this project is located by:

- Copying file path
- Type in terminal: `cd `
- Paste your file path
- Press Enter

## First time?

Run the following commands:

- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install moviepy`
- `pip install ffmpeg`
- `pip install ffmpeg-python`
- `brew install imagemagick`
- `pip install .`

## Steps

- Open terminal
- Type `add-timestamp`
- Navigate to the video you wish to timestamp and copy it.
- Type space followed by the name you wish your timestamped file to have in quotes("")
- Paste the path into the terminal
- Press enter

After the program executes, your video should be in the directory of this project in the videos folder.
