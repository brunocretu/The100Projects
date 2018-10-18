# FTP Program
#A file transfer program which can transfer files back and forth from a remote web sever.
#Based on: https://www.techinfected.net/2017/07/create-simple-ftp-server-client-in-python.html
#By Aman Deep

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    address = input("Server's address: ")
    port = input("Server's port: ")
    username = input("Client's username: ")
    password = input("Client's password: ")
    path = ('Server folder: ')

    authorizer = DummyAuthorizer()
    authorizer.add_user(username, password, path, perm='elradfmw')
    authorizer.add_anonymous(path, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer((address, port), handler)
    server.serve_forever()

if __name__ == '__main__':
    main()
