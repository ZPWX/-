import socket
from socket import *
# socket.socket(AddressFamily, Type)
# 创建套节字
udp_socket = socket(socket.AF_INET, socket.SOCK_STREAM)
# 准备接收方的地址
# ‘192.168.1.103’目的地址
# 8080表示目的端口
dest_addr = ('192.168.1.103',8080)
# 从键盘获取数据
send_data = input("请输入要发送的数据：")
# 发送数据到指定的电脑上的指定程序
udp_socket.sendto(send_data.encode('utf-8'),dest_addr)
# 关闭套接字
udp_socket.close()
