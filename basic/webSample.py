import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(("www.py4inf.com",80))
mysocket.send("GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n")
# mysocket.send("GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n")

while True:
    data = mysocket.recv(512)
    if (len(data) < 1):
        break
    print(data)

mysocket.close()
