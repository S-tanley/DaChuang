from ultralytics import YOLO

# Load a model
model = YOLO('train8_best.pt')
results = model('rtsp://admin:miice520@192.168.200.24:554/Streaming/Channels/101')

for result in results:
    print(result.probs)

