import time
import cv2
from ultralytics import YOLO

model = YOLO('train8_best.pt')

def get_url(room_num):
    switcher = {
        1: "/Users/zhengbowen/nondefault/DaChuang_local/output.mp4",
        208: "rtsp://admin:miice520@192.168.200.20:554/Streaming/Channels/101",
        209: "rtsp://admin:miice520@192.168.200.21:554/Streaming/Channels/101",
        214: "rtsp://admin:miice520@192.168.200.22:554/Streaming/Channels/101",
        213: "rtsp://admin:miice520@192.168.200.23:554/Streaming/Channels/101",
        211: "rtsp://admin:miice520@192.168.200.24:554/Streaming/Channels/101",
        202: "rtsp://admin:miice520@192.168.200.25:554/Streaming/Channels/101",
        203: "rtsp://admin:miice520@192.168.200.26:554/Streaming/Channels/101",
        212: "rtsp://admin:miice520@192.168.200.27:554/Streaming/Channels/101",
        210: "rtsp://admin:miice520@192.168.200.28:554/Streaming/Channels/101"
    }
    return switcher[room_num]

def detect(room_num, delay, number):
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
        if (int(time.strftime("%S", time.localtime())) % delay == 0):  # 每5s截图
            results = model(frame)
            for result in results:
                if (result.probs.top1==1):
                    with open('example.txt', 'a') as f:
                        res = "The device in " + str(room_num) + " is on\n"
                        f.write(res)
                else:
                    with open('example.txt', 'a') as f:
                        res = "The device in " + str(room_num) + " is not on\n"
                        f.write(res)
            flag += 1
        if (flag == number):
            break
        # if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q退出
        #     break
    cv2.destroyAllWindows()  # 全屏显示

def check_rtsp(room_num):
    cap = cv2.VideoCapture(get_url(room_num))
    if cap.isOpened():
        with open('check_rtsp.txt', 'a') as f:
            res = "The rtsp address of the creame in " + str(room_num) + " is valid\n"
            f.write(res)
        return True
    else:
        with open('check_rtsp.txt', 'a') as f:
            res = "The rtsp address of the creame in " + str(room_num) + " is not valid\n"
            f.write(res) 
        return False

# 测试
if __name__ == '__main__':
    detect(1, 1, 1)



# match room_num: #python 3.10才有
    #     case 1:
    #         return "/Users/zhengbowen/nondefault/DaChuang_local/datasets/Processesdata/test/0/2031.png'"
    #     case 208:
    #         return "rtsp://admin:miice520@192.168.200.20:554/Streaming/Channels/101"
    #     case 209:
    #         return "rtsp://admin:miice520@192.168.200.21:554/Streaming/Channels/101"
    #     case 213:
    #         return "rtsp://admin:miice520@192.168.200.23:554/Streaming/Channels/101"
    #     case 211:
    #         return "rtsp://admin:miice520@192.168.200.24:554/Streaming/Channels/101"
    #     case 202:
    #         return "rtsp://admin:miice520@192.168.200.25:554/Streaming/Channels/101"
    #     case 203:
    #         return "rtsp://admin:miice520@192.168.200.26:554/Streaming/Channels/101"
    #     case 212:
    #         return "rtsp://admin:miice520@192.168.200.27:554/Streaming/Channels/101"