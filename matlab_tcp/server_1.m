
% 获取主机名和地址
[~, hostname] = system('hostname');
hostname = string(strtrim(hostname));
address = resolvehost(hostname, "address");

fprintf('hostname: %s, address: %s\n', address, hostname);


% 使用计算机地址和端口5000创建 tcpserver 对象。
% 创建一个名为 connectionFcn 的回调函数，以便在 TCP/IP 客户端连接到服务器时写入数据。
% 将 ConnectionChangedFcn 属性设置为回调函数 ConnectionFcn。
server = tcpserver(address, 2000, "ConnectionChangedFcn", @connectionFcn);


% 创建一个名为 readDataFcn 的回调函数，以便在每次指定字节的数据可用时读取数据。
% 将读数据存储在 tcpserver 对象的 UserData 属性中。您可以在此示例的末尾找到 readDataFcn 函数。
% 设置回调函数以在每次收到7688字节的数据时触发。
configureCallback(server, "byte", 7688, @readDataFcn);


% Connection Callback Function to Write Binary Data
% 这个函数调用 write 将数据写入连接的 TCP/IP 客户端。
function connectionFcn(src, ~)
    if src.Connected
        disp("Client connection accepted by server.")
        data = membrane(1);
        write(src, data(:), "double");
    end
    end


% Data Available Callback Function to Read Binary Data
% 这个函数调用 read 来读取字节数。
function readDataFcn(src, ~)
    disp("Data was received from the client.")
    src.UserData = read(src, src.BytesAvailableFcnCount/8, "double");
    reshapedServerData = reshape(src.UserData, 31, 31);
    figure(2);
    surf(reshapedServerData);
    end
