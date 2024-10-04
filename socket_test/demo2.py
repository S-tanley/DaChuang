# server code for demo1.py
import socket
import json

# 设置服务器地址和端口
HOST = '0.0.0.0'  # 监听所有可用的网络接口
PORT = 65432      # 使用一个未被占用的端口

# 创建 socket 对象
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # 绑定服务器地址和端口
    server_socket.bind((HOST, PORT))
    
    # 开始监听连接
    server_socket.listen()
    
    print('等待客户端连接...')
    connection, address = server_socket.accept()
    with connection:
        print('连接已建立：', address)
        
        data = connection.recv(1024)
        print('收到消息：', data.decode("utf-8"))

        data = connection.recv(4) 
        print('收到消息：', int.from_bytes(data, byteorder='big'))

        data = connection.recv(1024)
        received_json = data.decode()
        received_array = json.loads(received_json)
        print('收到消息：', received_array)

        message = "消息已收到"
        connection.send(message.encode("utf-8"))