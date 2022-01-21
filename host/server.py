import errno
import http.server
import os
import socket
import socketserver
import sys
import threading
import tkinter
from turtle import colormode
from urllib.parse import quote

import pyqrcode


class QRwindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        # self.geometry("400x450")
        self.title("Scan the QR")
        self.exit_button = tkinter.Button(self, text="EXIT", command=self.destroy, activebackground='red', activeforeground='white',)
        self.exit_button.pack(ipadx=225, ipady=10, side=tkinter.BOTTOM)


def hostit(directory):

    socketserver.TCPServer.allow_reuse_address = True

    class Handler(http.server.SimpleHTTPRequestHandler):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

    with socketserver.TCPServer(("", 8010), Handler) as httpd:
        httpd.serve_forever()


def main():
    if len(sys.argv) == 1:
        raise NameError(f"Please provide the path to the file which is to be hosted.")

    if not os.path.isfile(sys.argv[1]):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), sys.argv[1])

    file = sys.argv[1]
    directory, file = os.path.split(file)

    host = socket.gethostname()
    ipad = socket.gethostbyname(host)

    url = f"http://{ipad}:8010/{quote(file)}"
    print(url)

    URL = pyqrcode.create(url)
    xbm = URL.xbm(scale=8)


    root = QRwindow()

    bmp = tkinter.BitmapImage(data=xbm)
    # bmp.config(background="white")

    label = tkinter.Label(image=bmp)
    label.pack()

    threading.Thread(target=hostit, args=(directory, )).start()

    root.mainloop()


if __name__ == "__main__":

    # DEBUGGING
    sys.argv = ['', '/home/jithin/temp/ubuntu-18.04.6-desktop-amd64.iso']
    main()
