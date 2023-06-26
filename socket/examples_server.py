import socket
import threading
import time


def recv_info(client):  # SOCKET的接收函数
    count = 0
    while True:
        # 接收客户端信息
        data = client.recv(1024)
        print(data.decode())

        # 四次挥手，关闭服务端
        if len(data) == 0:
            client.send('bye'.encode())
            break

        # 向客户端发送信息
        info = 'server_feedback:' + str(count)
        client.send(info.encode())
        count += 1


if __name__ == "__main__":
    # 创建使用IPV4(socket.AF_INET)、TCP(socket.SOCK_STREAM)协议的套接字
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 监听本地的8898端口
    serversocket.bind(('0.0.0.0', 8898))

    # 开始接受连接
    serversocket.listen(5)

    # while True:
    # 完成三次握手，创建与客户端绑定，并进行通信的套接字，线程在此阻塞
    client, addr = serversocket.accept()

    t = threading.Thread(target=recv_info, args=(client,))
    t.start()

    # 关闭客户端链接
    client.close()

    # 关闭服务器套接字
    serversocket.close()    
