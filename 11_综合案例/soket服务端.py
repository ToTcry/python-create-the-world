import socket

socket_server = socket.socket()
socket_server.bind(('localhost', 8888))

socket_server.listen(1)

# result : tuple= socket_server.accept()
# conn = result[0]
# address = result[1]
conn, address = socket_server.accept()

print('客户端地址：', address)

data = conn.recv(1024).decode('utf-8')

print('客户端发送的数据：', data)

msg = input('输入回复消息').encode('utf-8')

conn.send(msg)
conn.close()




if __name__ == '__main__':
    pass

