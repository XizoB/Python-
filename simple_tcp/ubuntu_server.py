import socket
import threading
import argparse
import time


class ClientThread(threading.Thread):
    def __init__(self, dataSocket, addr):
        threading.Thread.__init__(self)
        self.sock = dataSocket
        self.addr = addr

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
                    print(f'接收到客户端消息: {data.decode()}')
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