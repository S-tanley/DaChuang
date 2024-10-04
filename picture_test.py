from ultralytics import YOLO

model = YOLO('yolov8n.pt')
picture_path = "/Users/zhengbowen/nondefault/DaChuang_local/output_video/211/2024-04-11-17-03-18.jpg"
results = model(picture_path) 
for r in results:
    r.save('results.jpg')