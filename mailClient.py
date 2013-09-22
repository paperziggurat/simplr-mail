import socket, ssl, base64

print ”I love computer networks!”

# Choose a mail server (e.g. Google mail server) and call it mailserver

mailserver = ('imap.gmail.com', 993)

# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start  

sslSocket = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM),

ssl_version = ssl.PROTOCOL_SSLv23)

sslSocket.connect(mailserver)

recv = sslSocket.recv(1024)

print recv