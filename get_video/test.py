import datetime
import os.path
import time
import cv2

def get_img_from_camera_net(folder_path, url, delay, number):
    """
    rstp截图保存, 按q退出
    :param folder_path: 保存位置
    :param url: rstp地址
    :param delay: 间隔几秒保存一次
    :param number: 保存多少张图片
    :return:
    """
    # 创建文件夹
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    cap = cv2.VideoCapture(url)
    ret, frame = cap.read()
    flag = 0
    while (ret):
        ret, frame = cap.read()
        # 不实时显示监控画面
        # cv2.imshow("frame", frame)
        file = folder_path + "{}.jpg".format(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))  # 以日期来命名文件并指定文件夹
        if (os.path.isfile(file) == False and int(time.strftime("%S", time.localtime())) % delay == 0):  # 每5s截图
            cv2.imwrite(file, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])  # 无损输出图片 但是图片质量仍不是很高
            print(file)
            flag += 1
        if (flag == number):
            break
        # if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q退出
        #     break
    cv2.destroyAllWindows()  # 全屏显示


# 测试
if __name__ == '__main__':
    #url = "rtsp://admin:miice520@192.168.200.21:554/Streaming/Channels/101" #209云台
    url = "rtsp://admin:miice520@192.168.200.24:554/Streaming/Channels/101" #211云台
    folder_path = 'output_video/211/'
    get_img_from_camera_net(folder_path, url, 3)