#-*-coding:utf-8-*-
from http import server
import socket
import selectors


def handle_read(io, sock, mask):
    if mask & selectors.EVENT_READ == 0:
        print("unhandled event.")
        return

    data = sock.recv(1024)
    if len(data) == 0:
        print("client close connection.")
        io.unregister(sock)
        sock.close()
    else:
        print(f'recv client data: {data}')

def handle_accept(io, sock, mask):
    if mask & selectors.EVENT_READ == 0:
        print("unhandled event.")
        return

    client, addr = sock.accept()
    io.register(client, selectors.EVENT_READ, handle_read)
 
def run_server_fix():
    # 创建使用IPV4(socket.AF_INET)、TCP(socket.SOCK_STREAM)协议的套接字
    sel = selectors.DefaultSelector()


    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #监听本地的8080端口
    serversocket.bind(('0.0.0.0', 8080))

    #开始接受连接
    serversocket.listen(5)
    sel.register(serversocket, selectors.EVENT_READ, handle_accept)

    while True:
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(sel, key.fileobj, mask)
       
def main():
    run_server_fix()

if __name__ == '__main__':
    main()