# client code
import socket
import json

# HOST = '10.135.240.33'
HOST = '8.137.86.205'
PORT = 65432

def tcp_client():
    # 创建TCP Socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接到服务器
    client_socket.connect((HOST, PORT))

    # 发送消息
    # message = 'Hello, server!' #string 
    # client_socket.send(message.encode("utf-8"))

    # message = 1 # int 
    # client_socket.send(message.to_bytes(4, byteorder='big'))

    # message = [1, 2, 3, 4, 5] # array
    # json_data = json.dumps(message)
    # client_socket.send(json_data.encode())

    # 接收数据
    message = client_socket.recv(1024).decode("utf-8")
    print(f"Message from server: {message}")

    # 关闭Socket
    client_socket.close()

if __name__ == '__main__':
    tcp_client()