import socket
import threading
import argparse
import time
import struct



"""
字符串(str): 这是最常见的数据类型,适用于大多数文本通信。
在传输前, 字符串可以编码为字节串(bytes), 例如使用UTF-8编码。

字节串(bytes): 在socket编程中, 字节串用于二进制数据的传输。
它可以包含任何类型的数据，包括文本和二进制数据。

字节数组(bytearray): 字节数组是字节串的不可变版本，
它允许你在不创建新字节串的情况下修改数据。

结构体(struct): 使用struct模块, 你可以将Python中的基本数据类型组合成一个结构体,
以便在socket通信中发送复杂的数据。

列表(list):列表可以包含任何类型的数据,包括字符串、字节串等。
在socket通信中,列表可以用来传输多组数据。

字节对象(memoryview): 通过memoryview, 你可以创建一个内存视图，
对内存进行高效的数据访问，特别是在处理大量数据时。
"""


class ClientThread(threading.Thread):

    def __init__(self, dataSocket, addr):
        threading.Thread.__init__(self)
        self.sock = dataSocket
        self.addr = addr
        self.format = 'if'


    def run(self):
        # --- 接受客户端消息,并向客户端发送消息
        count = 0
        while True:
            try:
                response = "服务端回应-{}".format(count)
                count += 1
                self.sock.send(response.encode())   # 向客户端发送消息

                data = self.sock.recv(1024)         # 接收客户端的消息
                if len(data) == 0:
                    self.sock.close()               # 四次挥手，关闭服务端
                    continue
                else:
                    unpacked_data = struct.unpack(self.format, data)
                    print(f'接收到客户端消息: {unpacked_data}')
                time.sleep(1)

            except Exception as e:
                print(f'Catch all exception: {e}')
                print('客户端 {} 关闭, 关闭相应的dataSocket.'.format(self.addr))
                self.sock.close()                   # 四次挥手，关闭服务端
                break


def ubuntu_server(args):
    # --- 实例化一个socket对象并指明协议:
    # 使用IPV4(socket.AF_INET)、TCP(socket.SOCK_STREAM)协议的socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # --- socket绑定IP地址和端口, 监听xx地址的xx端口
    # 127.0.0.1(localhost):50000    ->  localhost:*
    serversocket.bind((args.IP, args.SERVER_PORT))

    # --- 使socket处于监听状态，等待客户端的连接请求
    # 参数 5 表示最多接受多少个等待连接的客户端
    serversocket.listen(5)


    clients = []
    while True:
        # 完成三次握手，与客户端绑定，并进行通信的套接字
        # 127.0.0.1(localhost):50000    ->  127.0.0.1(localhost):xxxx 
        dataSocket, addr = serversocket.accept()
        print('接受一个客户端连接:', addr)


        t = ClientThread(dataSocket, addr)
        clients.append(t)
        t.start()


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
    ubuntu_server(args)