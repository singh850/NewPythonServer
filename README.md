# NewPythonServer

⚫️ In new Python code these are the errors I got- 

Unhandled exception in thread started by <function handler at 0x1036dbd70>
Traceback (most recent call last):
  File "/Users/tikamsingh/Desktop/Dateserver.py", line 22, in handler
    data = clientsocket.recv(1024)
socket.error: [Errno 54] Connection reset by peer

Unhandled exception in thread started by <function push at 0x1036eda28>
Traceback (most recent call last):
  File "/Users/tikamsingh/Desktop/Dateserver.py", line 30, in push
    i.send("Curent date and time: " + str(datetime.datetime.now().time()) + '\n')
socket.error: [Errno 32] Broken pipe
[Cancelled]

⚫️ Need a Code like:

def handler(clientsocket, clientaddr):
    data = clientsocket.recv(buf)
    print(data)
    while True:
        if data=='U' or 'UP':
            msg="Led ON" # if conditions match I want to send String back to my Android phone
            push(msg)
        if data=='D' or 'DOWN':
            msg="Led OFF" # if conditions match I want to send String back to my Android phone
            push(msg)
        else:
            break
        break
        
# Server set to always Listning either app closed or Opend or ReOpend.
