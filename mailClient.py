#AARON SAMS & WES CARTER - IMAP CLIENT
import socket, ssl, base64, getpass, os, platform
#--------------------------------------
mailserver = ('imap.gmail.com', 993)	
#--------------------------------------
sslSocket = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), 
ssl_version = ssl.PROTOCOL_SSLv23)
sslSocket.connect(mailserver)
recv = sslSocket.recv(1024)
print recv
#--------------------------------------

#PROMPT USER FOR USERNAME
def getuser():
	user = raw_input('Enter username (gmail): ')
	return user
	
#MENU DISPLAY
def menu(user, passwd):
	if platform.system() == 'Windows': #CLEARS TERMINAL/COMMAND PROMPT FOR A MORE VISUALLY FRIENDLY UI
		os.system('cls')
	else:
		os.system('clear') 
		
	print '--------------------------------------------------------------------------'
	print 'Welcome, ' + user + '. Please select an option from the list below: '
	print '--------------------------------------------------------------------------'
	print ' 1) LIST \n 2) SEARCH \n 3) FETCH \n 4) EXAMINE \n 5) CREATE \n 6) DELETE \n 7) UID'
	print '--------------------------------------------------------------------------'
	print '--------------------------------------------------------------------------'
	choice = raw_input('-> ')
	if choice == '1':
		list(user, passwd)
	if choice == '2':
		search(user, passwd)
	if choice == '3':
		fetch(user, passwd)
	if choice == '4':
		examine(user, passwd)
	if choice == '5':
		create(user, passwd)
	if choice == '6':
		delete(user, passwd)
	if choice == '7':
		uid(user, passwd)
	else:
		print choice + 'is not a valid option.  Please try again: '
		menu(user, passwd)
	return

#LOOP MENU	
def loopmenu(user, passwd):
	choice = raw_input('Back to menu? ')
	if choice.lower() in ['y', 'yes']:
		menu(user, passwd)
	if choice.lower() in ['n', 'no']:
		print 'END'
	else:
		print 'Please enter YES or NO'
		loopmenu(user,passwd)

#LOGIN		
def login(user, passwd):
	sslSocket.send('A001 LOGIN ' + user + ' ' + passwd + '\r\n')
	recv = sslSocket.recv(1024)
	print recv
	return
	
#LIST MAILBOXES
def list(user, passwd):
	mailbox = raw_input('Mailbox to list, ("/" to list root mailbox): ')
	sslSocket.send('A001 LIST "'+ mailbox +'" *\r\n')
	recv = sslSocket.recv(1024)
	print recv
	loopmenu(user, passwd)
	return

#SEARCH MAILBOX FOR MAIL CONTAINING SERCH TERMS
def search(user, passwd):
	mailbox = raw_input('Enter the name of the mailbox you wish to search: ')
	sslSocket.send('A001 EXAMINE ' + mailbox + '\r\n')
	recv = sslSocket.recv(1024)
	print recv
	search = raw_input('Enter search terms: ')
	sslSocket.send('A002 SEARCH ' + search + '\r\n')
	recv = sslSocket.recv(1024)
	print recv
	loopmenu(user, passwd)
	return

#FETCH FUNCTION FIRST EXAMINES MAILBOX TO FETCH FROM, THEN FETCHES HEADER + BODY	
def fetch(user, passwd):
	mailbox = raw_input('Enter the name of the mailbox from which you wish to fetch: ')
	sslSocket.send('A001 EXAMINE ' + mailbox + '\r\n')
	recv = sslSocket.recv(1024)
	print recv
	email = raw_input ('Enter email to fetch: ')
	sslSocket.send('A002 FETCH ' + email + ' BODY[0]\r\n') #FETCH HEADER
	recv = sslSocket.recv(1024)
	print recv 
	print '\n\n'
	sslSocket.send('A003 FETCH ' + email + ' BODY[1]\r\n') #FETCH BODY
	recv = sslSocket.recv(1024)
	print recv
	loopmenu(user, passwd)
	return

#EXAMINE FUNCTION	
def examine(user, passwd):
	pattern = raw_input('Enter name of mailbox to examine: ')
	sslSocket.send('A001 EXAMINE ' + pattern + '\r\n')
	recv = sslSocket.recv(1024)
	print recv
	loopmenu(user, passwd)
	return

#CREATE FUNCTION
def create(user, passwd):
	folder = raw_input('Enter the name of the folder you wish to create: ')
	sslSocket.send('A001 CREATE ' + pattern + '\r\n')
	recv = sslSocket.recv(1024)
	print recv
	loopmenu(user, passwd)
	return

#DELETE FUNCTION
def delete(user, passwd):
	delete = raw_input('Enter the name of the folder you wish to delete: ')
	sslSocket.send('A001 DELETE ' + pattern + '\r\n')
	recv = sslSocket.recv(1024)
	print recv
	loopmenu(user, passwd)
	return

#GET UID FUNCTION	
def uid(user, passwd):
	loopmenu(user, passwd)
	return

#MAIN	
if __name__ == '__main__':
	user = getuser()
	passwd = getpass.getpass()
	login(user, passwd)
	menu(user, passwd)
		