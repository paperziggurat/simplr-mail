#AARON SAMS & WES CARTER

#                __  .__                    .__                               .__  .__               __     #
# ______ ___.__._/  |_|  |__   ____   ____   |__| _____ _____  ______     ____ |  | |__| ____   _____/  |_  #
# \____ <   |  |\   __\  |  \ /  _ \ /    \  |  |/     \\__  \ \____ \  _/ ___\|  | |  |/ __ \ /    \   __\ #
# |  |_> >___  | |  | |   Y  (  <_> )   |  \ |  |  Y Y  \/ __ \|  |_> > \  \___|  |_|  \  ___/|   |  \  |   #
# |   __// ____| |__| |___|  /\____/|___|  / |__|__|_|  (____  /   __/   \___  >____/__|\___  >___|  /__|   # 
# |__|   \/                \/            \/           \/     \/|__|          \/             \/     \/       #
#																											#


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
	sslSocket.send('A002 LIST "'+ mailbox +'" *\r\n')
	recv = sslSocket.recv(1024)
	print recv
	
	loopmenu(user, passwd)
	return

#SEARCH MAILBOX FOR MAIL CONTAINING SERCH TERMS
def search(user, passwd):
	mailbox = raw_input('Enter the name of the mailbox you wish to search: ') 
	sslSocket.send('A003 EXAMINE ' + mailbox + '\r\n') #EXAMINE THIS MAILBOX FOR SEARCH
	recv = sslSocket.recv(1024)
	print recv
	
	search = raw_input('Enter search terms: ')
	sslSocket.send('A004 SEARCH ' + search + '\r\n') #SEARCH EXAMINED MAILBOX CONTAINING SEARCH TERMS
	recv = sslSocket.recv(1024)
	print recv
	
	loopmenu(user, passwd)
	return

#FETCH FUNCTION FIRST EXAMINES MAILBOX TO FETCH FROM, THEN FETCHES HEADER + BODY	
def fetch(user, passwd):
	mailbox = raw_input('Enter the name of the mailbox from which you wish to fetch: ')
	sslSocket.send('A005 EXAMINE ' + mailbox + '\r\n')
	recv = sslSocket.recv(1024)
	print recv
	
	email = raw_input ('Enter email to fetch: ')
	sslSocket.send('A006 FETCH ' + email + ' BODY[0]\r\n') #FETCH HEADER
	recv = sslSocket.recv(1024)
	print recv 
	
	print '\n\n'
	sslSocket.send('A007 FETCH ' + email + ' BODY[1]\r\n') #FETCH BODY
	recv = sslSocket.recv(1024)
	print recv
	
	loopmenu(user, passwd)
	return

#EXAMINE FUNCTION	
def examine(user, passwd):
	pattern = raw_input('Enter name of mailbox to examine: ')
	sslSocket.send('A008 EXAMINE ' + mailbox + '\r\n')
	recv = sslSocket.recv(1024)
	print recv
	
	loopmenu(user, passwd)
	return

#CREATE FUNCTION
def create(user, passwd):
	folder = raw_input('Enter the name of the folder you wish to create: ')
	sslSocket.send('A009 CREATE ' + folder + '\r\n')
	recv = sslSocket.recv(1024)
	print recv
	
	loopmenu(user, passwd)
	return

#DELETE FUNCTION
def delete(user, passwd):
	folder = raw_input('Enter the name of the folder you wish to delete: ')
	sslSocket.send('A010 DELETE ' + folder + '\r\n')
	recv = sslSocket.recv(1024)
	print recv
	
	loopmenu(user, passwd)
	return

#GET UID FUNCTION	
def uid(user, passwd):
	mailbox = raw_input('Mailbox for UID search/fetch: ') 
	sslSocket.send('A011 EXAMINE ' + mailbox + '\r\n') #EXAMINE THIS MAILBOX
	recv = sslSocket.recv(1024)
	print recv
	
	search = raw_input('Enter FLAG (e.g. TEXT, FROM, etc.) and search term (UID will be returned): ')
	sslSocket.send('A012 UID SEARCH ' + search + '\r\n') #SEARCH THIS MAILBOX WITH SEARCH TERMS
	recv = sslSocket.recv(1024)
	print recv
	
	uid = raw_input('Enter UID to fetch email: ')
	sslSocket.send('A013 UID FETCH ' + uid + '\r\n') #RETURN UID OF EMAIL CONTAINING SEARCH TERMS
	recv = sslSocket.recv(1024)
	print recv
	
	loopmenu(user, passwd)
	return

#MAIN	
if __name__ == '__main__':
	user = getuser()
	passwd = getpass.getpass() #HIDES USER PASSWORD
	login(user, passwd)
	menu(user, passwd)
		