import socket

#take the server name
host='localhost'

#take the port number
port=5000

#create a socket at server side using TCP/IP protocol
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket with server server and port numner
s.bind((host,port))

#allow maximum 1 connection to the socket
s.listen(1)

#wait till a client accepts connection
c, addr = s.accept()

#display client address
print("Connection from: ",str(addr))

#send messages to the client after encoding into binary string
c.send(b"Hello client, how are U")
msg="Bye!"
c.send(msg.encode())

#disconnecting the server
c.close()
