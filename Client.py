import socket

#take the server name
host='localhost'
#take the port number
port=5000

#create a socket at server side using TCP/IP protocol
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect it to server and port number
s.connect((host,port))
#receive message string from server, at a time 1024 B
msg = s.recv(1024)
#receive as long as message strings are not empty
while msg:
 print('Received: '+ msg.decode())
 msg = s.recv(1024)
