import errno
import http.server
import os
import socket
import socketserver
import sys
import threading
import tkinter
from urllib.parse import quote

import pyqrcode


class QRwindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scan the QR")

        self.exit_button = tkinter.Button(
            self,
            text="PRESS 'X' to EXIT OR CLICK HERE",
            command=self.destroy,
            activebackground="red",
            activeforeground="white",
        )
        self.exit_button.pack(ipadx=225, ipady=10, side=tkinter.BOTTOM)

    def close_window(self, event) -> None: self.destroy()


def hostit(directory):
    socketserver.TCPServer.allow_reuse_address = True

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

    with socketserver.TCPServer(("", 8010), Handler) as httpd:
        httpd.serve_forever()


def main():
    if len(sys.argv) == 1:
        raise Exception(f"Provide the path to the file which is to be hosted!")

    if not os.path.isfile(sys.argv[1]):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), sys.argv[1])

    file = sys.argv[1]
    directory, filename = os.path.split(file)

    ipaddress = socket.gethostbyname(socket.gethostname())

    url = f"http://{ipaddress}:8010/{quote(filename)}"
    print(url)

    root = QRwindow()
    bmp = tkinter.BitmapImage(data=pyqrcode.create(url).xbm(scale=8))

    label = tkinter.Label(image=bmp)
    label.pack()

    host_thread = threading.Thread(target=hostit, args=(directory,))
    host_thread.daemon=True 
    host_thread.start()

    root.bind("x", root.close_window)
    root.mainloop()


if __name__ == "__main__":
    main()
