#-*-coding:utf-8-*-
import socket
import time
import random


def run_client_fix():
    # 创建使用IPV4(socket.AF_INET)、TCP(socket.SOCK_STREAM)协议的socket
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #连接127.0.0.1:8080的服务器
    cli.connect(('127.0.0.1', 8080))

    name = 'client%d' % random.randint(1, 1000)
    while True:
        # 接收服务器的消息
        try:
            cli.send(name.encode())
            time.sleep(1)
        except ConnectionResetError as e:
            print('remote server is closed, close myself.')
            cli.close()
            break

def main():
    run_client_fix()

if __name__ == '__main__':
    main()