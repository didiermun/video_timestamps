# video_timestamps/add_timestamp.py

import argparse
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def add_timestamp(video_path, output_path):
    # load the video
    video = VideoFileClip(video_path)
    video_size = video.size

    # add a timestamp to each frame
    def add_time_to_frame(get_frame, t):
        frame = get_frame(t)
        timestamp_text = t_to_timestamp(t)
        timestamp_clip = TextClip(timestamp_text, fontsize=24, color='white', stroke_color='black', stroke_width=2)
        timestamp_clip = timestamp_clip.set_position(("left", "top")).set_duration(video.duration).set_start(t)

        frame_with_timestamp = CompositeVideoClip([video.set_position((0, 0)), timestamp_clip.set_position(("left", "top"))], size=video_size)
        return frame_with_timestamp.get_frame(t)

    # convert time to a timestamp string
    def t_to_timestamp(t):
        minutes = int(t // 60)
        seconds = int(t % 60)
        return f"{minutes:02d}:{seconds:02d}"

    # apply the function to each frame of the video
    timestamped_video = video.fl(add_time_to_frame)

    # Write the result to a file
    timestamped_video.write_videofile(output_path, codec='libx264')

def main():
    parser = argparse.ArgumentParser(description="Add timestamps to a video.")
    parser.add_argument('input_video_path', type=str, help="Path to the input video file.")
    parser.add_argument('output_video_path', type=str, help="Path to save the output video file with timestamps.")
    args = parser.parse_args()

    add_timestamp(args.input_video_path, args.output_video_path)

if __name__ == "__main__":
    main()
