# Inference(our GPU servers)
import time
import cv2
from ultralytics import YOLO
import socket
import json

model = YOLO('train8_best.pt') #choose the model we use
HOST = '10.135.240.33'
PORT = 65432

def detect_cls(picture):
    """
    rstp截图保存, 按q退出
    :param picture: the sorce picture we use to do inference(can be a list)
    :return: the class the model get
    """
    results = model(picture)
    res = []
    for result in results:
        res = res.append(result.probs.top1)
    return res

def tcp_server(res):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # 绑定服务器地址和端口
        server_socket.bind((HOST, PORT))
        
        # 开始监听连接
        server_socket.listen()
        
        print('Waiting for clients to connect...')
        connection, address = server_socket.accept()
        with connection:
            print('connection is estabished:', address)

            for i in res:


            #connection.send(b'消息已收到')

# 测试
if __name__ == '__main__':
    # detect(1, 1, 1)