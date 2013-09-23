import socket, ssl, base64, getpass, os

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('imap.gmail.com', 993)

# Create socket called clientSocket and establish a TCP connection with mailserver



#Fill in start  

#CONNECTION
sslSocket = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM),
ssl_version = ssl.PROTOCOL_SSLv23)
sslSocket.connect(mailserver)
recv = sslSocket.recv(1024)

#PROMPT USER FOR USERNAME
def getuser():
	user = raw_input('Username: ')
	return user

#MENU
def menu(user, passwd):
	os.system("clear")
	print '---------------------------------------------------------------------'
	print 'Welcome, ' + user + '.  Please select an option from the list below: '
	print '---------------------------------------------------------------------'
	print '(1) LIST\n(2) SEARCH\n(3) FETCH\n(4) EXAMINE\n(5) CREATE\n(6) DELETE\n(7) UID\n(8) LOGOUT'
	print '---------------------------------------------------------------------'
	choice = raw_input('-> ')
	if choice == '1':
		list()
	if choice == '2':
		search()
	if choice == '3':
		fetch()
	if choice == '4':
		examine()
	if choice == '5':
		create()
	if choice == '6':
		delete()
	if choice == '7':
		uid()
	if choice == '8':
		logout()
		
	return
	
#LOGIN
def login(user, passwd):
	sslSocket.send('A001 LOGIN ' + user + ' ' + passwd + '\r\n')
	recv = sslSocket.recv(1024)
	return
	
def list():
	sslSocket.send('')
	recv = sslSocket.recv(1024)
	print recv
	return
	
def search():
	return
	
def fetch():
	return
	
def examine():
	return
	
def create():
	return
	
def delete():
	return
	
def uid():
	return
	
#MAIN
if __name__ == '__main__':
	user = getuser()
	passwd = getpass.getpass()
	menu(user, passwd)
	login(user, passwd)

	
	