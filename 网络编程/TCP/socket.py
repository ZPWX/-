form socket import *
# 1.创建socket
tcp_client_socket = socket(AF_INET,SOCK_STREAM)
# 2.目的信息
server_ip = input("输入服务器ip地址：")
server_port = int(input("请输入服务器端口："))
# 3.连接服务器
tcp_client_socket.connect((server_ip, server_port))
# 4.提示用户输入数据
send-data = input("输入要发送的数据：")
tcp_client_socket.send(send-data.encode("gbk"))
# 5.接受对方发来的数据，最大接受1024字节
recvData = tcp_client_socket.recv(102400)
print('接受到的数据：'，recvData.decode('gbk'))
# 6.关闭套接字
tcp_client_socket.close()
