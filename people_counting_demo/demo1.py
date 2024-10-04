import time
import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

def get_url(room_num):
    switcher = {
        1: "/Users/zhengbowen/Downloads/test1.mp4",
        208: "rtsp://admin:miice520@192.168.200.20:554/Streaming/Channels/101",
        209: "rtsp://admin:miice520@192.168.200.21:554/Streaming/Channels/101",
        213: "rtsp://admin:miice520@192.168.200.23:554/Streaming/Channels/101",
        211: "rtsp://admin:miice520@192.168.200.24:554/Streaming/Channels/101",
        202: "rtsp://admin:miice520@192.168.200.25:554/Streaming/Channels/101",
        203: "rtsp://admin:miice520@192.168.200.26:554/Streaming/Channels/101",
        212: "rtsp://admin:miice520@192.168.200.27:554/Streaming/Channels/101"
    }
    return switcher[room_num]

def people_count(room_num, delay, number):
    """
    rstp截图保存, 按q退出
    :param room_num: 教室号地址
    :param delay: 间隔几秒保存一次
    :param number: 保存多少张图片
    :return:
    """
    url = get_url(room_num) #rtsp地址

    cap = cv2.VideoCapture(url)
    ret, frame = cap.read()
    flag = 0
    while (ret):
        ret, frame = cap.read()
        # 不实时显示监控画面
        # cv2.imshow("frame", frame)
        if (int(time.strftime("%S", time.localtime())) % delay == 0):  # 每 delay s截图
            results = model(frame)
            with open('example.txt', 'a') as f:
                for result in results:
                    line = result.verbose()
                    parts = line.strip().split(', ')
                    for part in parts:
                        if 'persons' in part:
                            res = part + "in room " + str(room_num)
                            f.writelines(res)
                            break
                    else:
                        res = "0 people in room " + str(room_num)
                        f.writelines(res) 
                    f.write('\n')
            flag += 1
        if (flag == number):
            break
        # if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q退出
        #     break
    cv2.destroyAllWindows()  # 全屏显示


# 测试
if __name__ == '__main__':
    people_count(1, 1, 3)
