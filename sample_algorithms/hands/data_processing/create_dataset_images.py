import cv2
import os

split = 'train'
# Input and output folder paths
video_folder = f"videos/{split}"
output_folder = f"coco/{split}"

# Ensure output directory exists
os.makedirs(output_folder, exist_ok=True)

# Iterate through all files in the video folder
for video_file in sorted(os.listdir(video_folder)):
    if video_file.endswith((".mp4", ".MP4")):  # Add other formats if needed
        video_path = os.path.join(video_folder, video_file)
        video_name = os.path.splitext(video_file)[0]  # Get video name without extension
        
        cap = cv2.VideoCapture(video_path)
        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break  # Stop if end of video is reached
            
            frame_filename = f"{video_name}_frame_{frame_count:05d}.jpg"  # Format: videoName_frame0001.jpg
            frame_path = os.path.join(output_folder, frame_filename)
            
            cv2.imwrite(frame_path, frame)
            frame_count += 1

        cap.release()
        print(f"Extracted {frame_count} frames from {video_file}")

print("Frame extraction completed.")
