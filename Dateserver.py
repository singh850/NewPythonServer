from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import thread
import time
import datetime

host = '0.0.0.0'
port = 5555
buf = 2048

addr = (host, port)

serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serversocket.bind(addr)
serversocket.listen(10)

clients = [serversocket]

def handler(clientsocket, clientaddr):
    print "Accepted connection from: ", clientaddr
    while True:
        data = clientsocket.recv(1024)
        print (data)
        

def push():
    while True:
        for i in clients:
            if i is not serversocket: # neposilat sam sobe
                i.send("Curent date and time: " + str(datetime.datetime.now().time()) + '\n')
        time.sleep(1) # [s]


thread.start_new_thread(push, ())

while True:
    try:
        clientsocket, clientaddr = serversocket.accept()
        clients.append(clientsocket)
        thread.start_new_thread(handler, (clientsocket, clientaddr))
    except KeyboardInterrupt: # Ctrl+C # FIXME: vraci "raise error(EBADF, 'Bad file descriptor')"
        print ("Closing server socket...")
        serversocket.close()