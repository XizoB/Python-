import socket
import time


def main():
    # 创建使用IPV4(socket.AF_INET)、TCP(socket.SOCK_STREAM)协议的socket
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接127.0.0.1:8898的服务器
    cli.connect(('127.0.0.1',8898))

    count = 0
    while True:
        # 向服务器发送消息
        info = "client_send:" + str(count)
        cli.send(info.encode())
        time.sleep(1)

        # 接收服务器的消息
        data = cli.recv(1024)

        # 四次挥手，关闭客户端
        if data == b'bye':
            cli.send(b'bye')
            break
        print(data.decode())
        count += 1

    # 关闭客户端套接字
    cli.close()

if __name__ == '__main__':
    main()