import cv2

for ip in range(122, 256):
    url = f"rtsp://admin:miice520@192.168.200.{ip}:554/Streaming/Channels/101"
    # url = f"rtsp://admin:miice520@192.168.200.{ip}:554/Streaming/Channels/101"
    cap = cv2.VideoCapture(url)
    if cap.isOpened():
        with open('check_ip.txt', 'a') as f:
            res = "The rtsp address of the creame in " + str(ip) + " is valid\n"
            f.write(res)
    else:
        with open('check_ip.txt', 'a') as f:
            res = "The rtsp address of the creame in " + str(ip) + " is not valid\n"
            f.write(res) 
