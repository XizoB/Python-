#-*-coding:utf-8-*-
import socket


def run_server():

    # 创建使用IPV4(socket.AF_INET)、TCP(socket.SOCK_STREAM)协议的套接字
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 监听本地的8080端口
    serversocket.bind(('127.0.0.1', 8080))

    # 开始接受连接
    serversocket.listen(5)

    # 完成三次握手，创建与客户端绑定，并进行通信的套接字
    client, addr = serversocket.accept()
    
    while True:
        # 服务器接收客户端发送的消息
        data = client.recv(1024)

        # 四次挥手，关闭服务端
        if len(data) == 0:
            print("clint close this socket.")
            client.close()
            break
        print(f'server recv data is : {data.decode()}')

        # 服务器发送消息给客户端
        client.send('world'.encode())
    

def main():
    run_server()

if __name__ == '__main__':
    main()