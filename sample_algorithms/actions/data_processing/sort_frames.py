import os
import shutil
import pandas as pd

input_dir = "path to folder with extracted frames"       
output_dir = "path to folder with sorted frames"   
annotations = pd.read_csv("path to viodeo annotations")

print(annotations)


for i in range(len(annotations["start_frame"])):
    os.makedirs(os.path.join(output_dir, annotations["clip_id"][i]))
    index = 0
    for j in range(annotations["start_frame"][i], annotations["stop_frame"][i]+1):
        frame_id = "frame_"+str(j).zfill(5)
        print(frame_id)
        img_path = os.path.join(os.path.join(input_dir, annotations["video_id"][i]),frame_id+".jpg")
        out_id = "img_"+str(index).zfill(5)
        out_path = os.path.join(os.path.join(output_dir, annotations["clip_id"][i]),out_id+".jpg")
        print(out_path)
        shutil.copy2(img_path, out_path)
        index = index+1





