from ultralytics import YOLO
import cv2

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Define path to video file
video_path = "/Users/zhengbowen/datasets/test_video.mp4"

results = model(video_path, stream=True)  # generator of Results objects

with open('/public/home/2022141520163/yolov8/runs/video_train/example1.txt', 'a') as f:
    for result in results:
        line = result.verbose()
        parts = line.strip().split(', ')
        for part in parts:
            if 'persons' in part:
                f.writelines(part)
                break
        else:
            f.writelines('0 persons') 
        f.write('\n')
