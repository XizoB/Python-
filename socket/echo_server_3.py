#-*-coding:utf-8-*-
import socket


def run_server_fix():

    # 创建使用IPV4(socket.AF_INET)、TCP(socket.SOCK_STREAM)协议的套接字
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #监听本地的8080端口
    serversocket.bind(('0.0.0.0', 8080))

    #开始接受连接
    serversocket.listen(5)
    clients = []
    
    while True:
        #服务器发送消息给客户端
        # 完成三次握手，创建与客户端绑定，并进行通信的套接字
        client, addr = serversocket.accept()
        clients.append(client)

        invalid_clients = []
        for cli in clients:
            data = cli.recv(1024)
            if len(data) == 0:
                print('remote client is closed, close myself.')
                invalid_clients.append(cli)
                cli.close()
                continue
            else:
                print(f'recv data {data}')
        
        for invalid_cli in invalid_clients:
            clients.remove(invalid_cli)

    
def main():
    run_server_fix()

if __name__ == '__main__':
    main()