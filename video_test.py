from ultralytics import YOLO
import cv2

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Define path to video file
video_path = "/Users/zhengbowen/datasets/test_video_s.mp4"
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
hight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('output4.mp4', fourcc, fps, (width, hight))

# Run inference on the source
results = model(video_path, stream=True)  # generator of Results objects

for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    # result.show()  # display to screen
    print(result.verbose())
    # result.save_txt('/public/home/2022141520163/yolov8/runs/video_train/test.txt')
    annotated_frame = result[0].plot()
    output_video.write(annotated_frame)


cap.release()
output_video.release()
cv2.destroyAllWindows()
