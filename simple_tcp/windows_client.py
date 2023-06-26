#-*-coding:utf-8-*-
import socket
import time
import random
import argparse


def windows_client(args):
    # --- 实例化一个socket对象并指明协议
    # 使用IPV4(socket.AF_INET)、TCP(socket.SOCK_STREAM)协议的socket
    dataSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # --- 连接服务端 socket
    # localhost:xxxx    ->  127.0.0.1(localhost):50000
    dataSocket.connect((args.IP, args.SERVER_PORT))
    

    # --- 向服务端发送消息,并接收服务端消息
    name = '客户端-{}'.format(random.randint(1, 1000))
    while True:
        try:
            dataSocket.send(name.encode())          # 向服务端发送消息，也要编码为 bytes

            recved = dataSocket.recv(args.BUFLEN)   # 接收服务端的消息
            if not recved:                          # 如果返回空bytes，表示对方关闭了连接
                continue
            print(recved.decode())
            time.sleep(1)
                
        except Exception as e:
            print(f'Catch exception: {e}')
            print('远程服务端关闭, 关闭自己.')
            dataSocket.close()
            break


if __name__ == '__main__':
    # --- 初始化参数
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--balabala",
        type=str,
        help="balabala",
    )
    args = parser.parse_args()


    # --- 定义参数
    args.IP = '127.0.0.1'
    args.SERVER_PORT = 50000
    args.BUFLEN = 1024


    # --- 运行客户端
    windows_client(args)