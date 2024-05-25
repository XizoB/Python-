close all;clear;clc;
data = randi(10,4096,2048);
config = whos('data');
package_num = 68860; %接收数据包的个数
time_out = 0.5; % 空数据包的等待时间
tcpipClient = tcpclient('127.0.0.1',1008, "Timeout", 5);%服务器地址
set(tcpipClient,'OutputBufferSize',65535);%数据包的大小
pause(0.5)
% set(tcpipClient,'Timeout',time_out);
% open(tcpipClient);
disp("连接成功")
disp("数据发送")
send_data = [config.size(:);data(:)];
config_send = whos('send_data');
write(tcpipClient,send_data,'double');
disp("数据接收")
recv_data = [];
h=waitbar(0,'正在接收数据');
for i=1:package_num  %因为一个数据包大小有限，需要重复多次接收
    recv_package = [];
    waitbar(i/package_num)
    while isempty(recv_package)
        recv_package=read(tcpipClient);
    end
    recv_data = vertcat(recv_data,recv_package);
end
close(h)
str = convertCharsToStrings(native2unicode(recv_data,'utf-8'));%解码出字典
try
    dic = jsondecode(str);%将json形式的字典数据里面的矩阵数据提取
    U=dic.U;
    S=dic.S;
    V=dic.V;
    re = U*diag(S)*V;%验证在python计算的结果是否和matlab算出来的一致
catch
    disp('WARNNING:接收数据包数量(package_num)设置太小')
end
disp('连接断开')
close(tcpipClient);