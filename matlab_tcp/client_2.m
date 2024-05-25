clc;
% 创建一个 tcpclient 实例，并将超时时间设置为5秒。
% 当使用两个 MATLAB 会话时，复制服务器的值。服务器地址和服务器。
% 并使用它们作为用于创建 tcpclient 对象的 Address 和 Port 值。
% client = tcpclient(server.ServerAddress, server.ServerPort,"Timeout",5);
client = tcpclient("192.168.0.103", 2000, "Timeout", 5);


pause(1);
NUM = 5;

% 接受服务端的数据

while (client.NumBytesAvailable > 0)
    rawData = read(client);
    rawData = native2unicode(rawData);
    fprintf("Clinet\t 与服务端 %s\n", rawData)
end


for i = 1:NUM
    % 向服务端发送数据
    send2server_data = rand(1,4,'double');
    write(client, send2server_data, "double");
    fprintf("Clinet\t 向服务端发送数据:\n")
    disp(send2server_data)

    % 接受服务端的数据
    receivefserve_data = read(client, 8, "double");
    fprintf("Clinet\t 接受服务端的数据:\n")
    disp(receivefserve_data)
end


clear client;