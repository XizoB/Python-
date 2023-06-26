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
        # 向服务器发送消息
        message = 'hello-' + str(count)
        cli.send(message.encode())
    
        # 接收服务器的消息
        data = cli.recv(1024)

        # 四次挥手，关闭客户端
        print(f'client recv server data {data}')
        count += 1
        time.sleep(1)
        if count >= 10:
            cli.close()
            break

def main():
    run_client()

if __name__ == '__main__':
    main()