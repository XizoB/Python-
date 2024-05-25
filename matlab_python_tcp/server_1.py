import socket
import numpy as np
import json
from progress.bar import Bar
#为了将numpy数组进行编码，准备一个json解析numpy数据类
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)
addr = ('127.0.0.1',1008) #设置服务端ip地址和端口号
buff_size = 65535 #消息的最大长度(适度调整可以增大数据传输速度)
package_num = 23845 #数据包数量(传输2048*4096 float32矩阵所需)
tcpSerSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSerSock.bind(addr)
tcpSerSock.listen(1)

while True:
    print('等待连接...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('连接到:', addr)

    while True:
        data = tcpCliSock.recv(int(buff_size))          #接收数据
        if not data:                                    #检测连接是否断开
            break
        decode = []                                     #存放解码后的数据
        with Bar('Processing', max=package_num) as bar: #进度条
            for i in range(package_num):
                print('%.2f'%(i/package_num*100)+'%')	#数据包接收进度
                recv_data = []
                while len(recv_data)==0:
                    data = tcpCliSock.recv(int(buff_size))
                recv_data = np.frombuffer(data,dtype='>f4') #数据解码
                #数据为4字节浮点(float32)，顺序为big-endian(>)。如接收完整float数据，则使用f8格式
                decode = np.append(decode,recv_data)        #数据拼接
                bar.next()
        print('接收到数据')
        height = int(decode[0])								#矩阵的行
        width = int(decode[1])								#矩阵的列
        echo = decode[2:int(height*width+2)]				#矩阵的数值
        mat = echo.reshape((height,width),order='F')		#按顺序重建矩阵,order参数决定了是行优先还是列优先。
        #完成计算任务
        U, S, V = np.linalg.svd(mat, full_matrices=False)   #奇异值分解
		#将计算结果（三个矩阵）打包为字典
        result={'U':U,
                'S':S,
                'V':V}
        send_result = json.dumps(result,cls=NpEncoder)      #将字典编码
        print('需要发回%d字节的数据包'%len(send_result))
        tcpCliSock.send(send_result.encode('utf-8'))        #数据发送
        break
    tcpCliSock.close()
tcpSerSock.close()