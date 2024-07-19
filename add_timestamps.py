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



input_video_path = "../A_Medium_Funkadesi061724_1[5'40-6'50]_1.mp4"
output_video_path = "output_video_with_timestamps.mp4"

add_timestamp(input_video_path, output_video_path)
