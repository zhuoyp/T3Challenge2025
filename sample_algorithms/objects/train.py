from ultralytics import YOLO
import os

if __name__ == '__main__':
    directory_path = "/path/to/train/script"
    os.chdir(directory_path)  # switch to the directory

    print(f"✅ Current Dictionary Path: {os.getcwd()}")

    # The yolo11n weight file is available below. 
    # https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt
    # The yolo11 config file is availble below. 
    # https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/models/11/yolo11.yaml
    model = YOLO("yolo11n.yaml").load("yolo11n.pt")

    # train model
    results = model.train(
        data="train.yaml",
        save_conf=True,
        show_conf=True,
        epochs=200,
        imgsz=640,
        device=0,
        batch=64,
        patience=50,
    )


