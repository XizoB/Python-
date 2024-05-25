% 创建一个 tcpclient 实例，并将超时时间设置为5秒。
% 当使用两个 MATLAB 会话时，复制服务器的值。服务器地址和服务器。
% 并使用它们作为用于创建 tcpclient 对象的 Address 和 Port 值。
% client = tcpclient(server.ServerAddress, server.ServerPort,"Timeout",5);
client = tcpclient("192.168.0.103", 2000, "Timeout", 5);


% pause(1);

% 接受服务端的数据
rawData = read(client, 961, "double");
reshapedData = reshape(rawData, 31, 31);
figure(1);
surf(reshapedData);

% 向服务端发送数据
write(client, rawData, "double");


clear client;