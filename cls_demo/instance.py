from demo1 import detect, check_rtsp
import sys

room_num = int(sys.argv[1])
if check_rtsp(room_num) is True: 
    detect(room_num, 1, 1)
else:
    print(f"The rtsp of the device in {room_num} is invalid")