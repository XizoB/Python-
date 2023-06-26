#-*-coding:utf-8-*-
import socket
import time


def run_server():

    # 创建使用IPV4(socket.AF_INET)、TCP(socket.SOCK_STREAM)协议的套接字
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #监听本地的8080端口
    serversocket.bind(('0.0.0.0', 8080))

    #开始接受连接
    serversocket.listen(5)

    # 完成三次握手，创建与客户端绑定，并进行通信的套接字
    client, addr = serversocket.accept()
    
    while True:
        #服务器发送消息给客户端
        client.send('world'.encode())

def run_server_2():

    # 创建使用IPV4(socket.AF_INET)、TCP(socket.SOCK_STREAM)协议的套接字
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #监听本地的8080端口
    serversocket.bind(('0.0.0.0', 8080))

    #开始接受连接
    serversocket.listen(5)

    # 完成三次握手，创建与客户端绑定，并进行通信的套接字
    client, addr = serversocket.accept()
    
    count = 0
    while True:
        #服务器发送消息给客户端
        client.send('world'.encode())
        count += 1
        if count >= 10:
            client.close()
            break

def run_server_fix():

    # 创建使用IPV4(socket.AF_INET)、TCP(socket.SOCK_STREAM)协议的套接字
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #监听本地的8080端口
    serversocket.bind(('0.0.0.0', 8080))

    #开始接受连接
    serversocket.listen(5)

    # 完成三次握手，创建与客户端绑定，并进行通信的套接字
    client, addr = serversocket.accept()
    
    while True:
        # 服务器发送消息给客户端
        try:
            client.send('world'.encode())
            time.sleep(1)
        except Exception as e:
            print(f'catch all exception: {e}')
            print('remote client is closed, close myself.')
            client.close()
            break
    

def main():
    run_server_fix()

if __name__ == '__main__':
    main()