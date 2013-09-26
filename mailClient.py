

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
print recv
 
#PROMPT USER FOR USERNAME
def getuser():
    user = raw_input('Enter your gmail Username (example MojoJoJo99 or MojoJoJo99@gmail.com ) : ')
    return user
 
#MENU
def menu(user, passwd):
# os.system("clear")
    print '---------------------------------------------------------------------'
    print 'Welcome, ' + user + '. Please select an option from the list below: '
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
#no log out command was needed for project
#     if choice == '8':
#             logout()
    return
 
#LOGIN
def login(user, passwd):
    sslSocket.send('A001 LOGIN ' + user + ' ' + passwd + '\r\n')
    recv = sslSocket.recv(1024)
    print recv
    return
 
def list():
    pattern = raw_input('Directory to list: ')
    sslSocket.send('A001 LIST "'+ pattern +'" *\r\n')
    recv = sslSocket.recv(1024)
    print recv
    return
#getting bad could not parse command if added \delete and uknown command when putting in ALL get A001 unknown command SEARCHALL dont know whats going on
def search():
    mailbox = raw_input('Enter the mailbox you want to search: ')
    sslSocket.send('A001 EXAMINE ' + mailbox +'\r\n')
    recv= sslSocket.recv(1024)
    print recv
    searchterm = raw_input('What would you like to search: ' )
    sslSocket.send('A002 SEARCH ' + searchterm + '\r\n')
    recv= sslSocket.recv(1024)
    print recv
    return  
   
 
def fetch():
    return
#examine just looks in the mailbox and returns either read or not read
def examine():  
    print 'Enter the name of the mailbox name you wish to look at'
    mailbox= raw_input('Enter mailbox name : ')
    sslSocket.send('A001 EXAMINE ' + mailbox + '\r\n')
    recv= sslSocket.recv(1024)
    print recv
    return
 
def create():
    print 'Type in the name of the folder you want to create.'
    mailbox = raw_input('Enter the folder name you want to create. ')
    sslSocket.send('A001 CREATE ' + mailbox + '\r\n')
    recv = sslSocket.recv(1024)
    print recv
    return
 
def delete():
    print 'Type in the name of the folder you want to delete.'
    mailbox = raw_input('Enter the folder name you want to destroy. ')
    sslSocket.send('A001 DELETE ' + mailbox + '\r\n')
    recv = sslSocket.recv(1024)
    print recv
    return
 
def uid():
    return
# def logout():
#     sslSocket.send('A023 lOGOUT "" *\r\n')
#     recv = sslSocket.recv(1024)
#     print recv    
#     return
 
#MAIN
if __name__ == '__main__':
        user = getuser()
        passwd = getpass.getpass()
        login(user, passwd)
        menu(user, passwd)



	
	