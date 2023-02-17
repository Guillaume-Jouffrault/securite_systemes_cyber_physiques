import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

host = s.getsockname()[0]
port = 5000

print("IP adress is :" + host)

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)

c, addr = s.accept()

print("CONNECTION FROM:", str(addr))

msg = c.recv(1024)
cpt_screen = 0
cpt_camera = 0
str = ""

while msg:
    if b'camera' in msg:
        cpt_camera += 1
        msg = msg[6:]
        str = 'camera'
    if b'screen' in msg:
        cpt_screen += 1
        msg = msg[6:]
        str = "screen"
    if str == "screen":
        with open(f'screen{cpt_screen}.png', 'ab') as file:
            file.write(msg)
            file.close()
    if str == "camera":
        with open(f'camera{cpt_camera}.png', 'ab') as file:
            file.write(msg)
            file.close()
    msg = c.recv(1024)

print(msg)

# disconnect the server
c.close()
