import argparse
import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def add_timestamp(video_path, output_path, start_time):
    # load the video
    video = VideoFileClip(video_path)
    video_size = video.size

    # convert start time from "min:secs" to seconds
    if start_time:
        start_min, start_secs = map(int, start_time.split(':'))
        start_time_secs = start_min * 60 + start_secs
    else:
        start_time_secs = 0

    # add a timestamp to each frame
    def add_time_to_frame(get_frame, t):
        frame = get_frame(t)
        current_time = t + start_time_secs

        timestamp_text = t_to_timestamp(current_time)
        timestamp_clip = TextClip(timestamp_text, fontsize=40, color='white', stroke_color='black', stroke_width=4)
        timestamp_clip = timestamp_clip.set_position(("left", "top")).set_duration(video.duration).set_start(t)

        frame_with_timestamp = CompositeVideoClip(
            [video.set_position((0, 0)), timestamp_clip.set_position(("left", "top"))],
            size=video_size
        )
        return frame_with_timestamp.get_frame(t)

    # convert time to a timestamp string
    def t_to_timestamp(t):
        minutes = int(t // 60)
        seconds = int(t % 60)
        return f"{minutes:02d}:{seconds:02d}"

    # apply the function to each frame of the video
    timestamped_video = video.fl(add_time_to_frame)

    # set the original audio to the new video
    timestamped_video = timestamped_video.set_audio(video.audio)

    # write the result to a file
    timestamped_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

def generate_output_path(file_path):
    directory, file_name = os.path.split(file_path)
    name, extension = os.path.splitext(file_name)
    new_file_name = f"{name}_output{extension}"
    new_file_path = os.path.join(directory, new_file_name)
    
    return new_file_path

def main():
    parser = argparse.ArgumentParser(description="Add timestamps to a video.")
    parser.add_argument('input_video_path', type=str, help="Path to the input video file.")
    parser.add_argument('--start_time', type=str, default='0:00', help="Optional start time in 'min:secs' format (e.g., '1:30').")
    # parser.add_argument('output_video_path', type=str, help="Path to save the output video file with timestamps.")
    args = parser.parse_args()

    add_timestamp(args.input_video_path, generate_output_path(args.input_video_path), args.start_time)

if __name__ == "__main__":
    main()
