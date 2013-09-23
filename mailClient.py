import socket, ssl, base64, getpass

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('imap.gmail.com', 993)

# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start  

#CONNECTION
########################################################################################################
sslSocket = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM),
ssl_version = ssl.PROTOCOL_SSLv23)
sslSocket.connect(mailserver)
recv = sslSocket.recv(1024)
########################################################################################################

#PROMPT USER FOR USERNAME
########################################################################################################
def getuser():
	user = raw_input('Username: ')
	return user

#MENU
########################################################################################################
def menu(user, passwd):
	print '---------------------------------------------------------------------'
	print 'Welcome, ' + user + '.  Please select an option from the list below: '
	print '---------------------------------------------------------------------'
	print recv
	return
	
#LOGIN
########################################################################################################
def login(user, passwd):
	return
	
#MAIN
########################################################################################################
if __name__ == "__main__":
	user = getuser()
	passwd = getpass.getpass()
	menu(user, passwd)

	
	