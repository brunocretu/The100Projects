# FTP Program
#A file transfer program which can transfer files back and forth from a remote web sever.
#Based on: https://www.techinfected.net/2017/07/create-simple-ftp-server-client-in-python.html
#By Aman Deep

from ftplib import FTP

address = input("Server address: ")
port = input("Server port: ")
#username = input("Username: ")
#password = input("Password: ")
path = input('Client folder: ')

ftp = FTP('')
ftp.connect(address, port)
ftp.login()
ftp.cwd(path)
ftp.retrlines('LIST')

def uploadFile():
    filename = input('File to upload: ')
    ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
    ftp.quit()

def downloadFile():
    filename = input('File to download: ')
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()

def main():
    question = input('Upload or Download? ')

    if question == 'U':
        uploadFile()
    else:
        downloadFile()

if __name__ == '__main__':
    main()
