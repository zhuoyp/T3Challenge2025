import cv2
import os
from moviepy import VideoFileClip
from PIL import Image

def extract_frames(video_path, output_folder, target_fps = 60):
    clip = VideoFileClip(video_path)

    duration = clip.duration  
    frame_times = [i / target_fps for i in range(int(duration * target_fps))]

    for i, t in enumerate(frame_times):
        frame = clip.get_frame(t)  
        image = Image.fromarray(frame).resize((480, 270)) 
        frame_path = os.path.join(output_folder, f"frame_{i:05d}.png")
        image.save(frame_path)
        print(f'Saved: {frame_path}')

video_paths = "path to extracted video frames"
for video_path in os.listdir(video_paths):
    os.makedirs('path to where video frames are stored' + video_path[:-4]) #make the folder
    output_folder = ("path to the folder where video frames are to be stored" #set the folder
                    + video_path[:-4])
    
    extract_frames("path to raw video folder"+video_path, output_folder) 
