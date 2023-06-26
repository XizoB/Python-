#-*-coding:utf-8-*-
import socket
import time

def run_client():
    # 创建使用IPV4(socket.AF_INET)、TCP(socket.SOCK_STREAM)协议的socket
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #连接127.0.0.1:8080的服务器
    cli.connect(('127.0.0.1', 8080))

    count = 0
    while True:
        # 接收服务器的消息
        data = cli.recv(1024)
        total_size = len(data)
        print(f'client recv server data {data}, bytes {total_size}\n')
        count += 1
        if count >= 10:
            cli.close()
            break

def run_client_2():
    # 创建使用IPV4(socket.AF_INET)、TCP(socket.SOCK_STREAM)协议的socket
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #连接127.0.0.1:8080的服务器
    cli.connect(('127.0.0.1', 8080))

    count = 0
    while True:
        # 接收服务器的消息
        data = cli.recv(1024)
        total_size = len(data)
        print(f'client recv server data {data}, bytes {total_size}\n')

def run_client_fix():
    # 创建使用IPV4(socket.AF_INET)、TCP(socket.SOCK_STREAM)协议的socket
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #连接127.0.0.1:8080的服务器
    cli.connect(('127.0.0.1', 8080))

    count = 0
    while True:
        # 接收服务器的消息
        data = cli.recv(1024)
        total_size = len(data)
        

        if total_size == 0:
            print('remote client socket is closed, close myself.')
            cli.close()
            break
        
        print(f'client recv server data {data}, bytes {total_size}')

def main():
    run_client_fix()

if __name__ == '__main__':
    main()