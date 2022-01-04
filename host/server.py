import os
import http.server
import socketserver
import socket
import threading
import pyqrcode
import sys
import tkinter

from urllib.parse import quote

def hostit(directory):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.TCPServer(('', 8010), Handler) as httpd:
        httpd.serve_forever()

def main():
    if len(sys.argv) == 1:
        raise ValueError("Please provide a path!")

    file = sys.argv[1]

    directory, file = os.path.split(file)

    host = socket.gethostname()
    ipad = socket.gethostbyname(host)

    url = f'http://{ipad}:8010/{quote(file)}'
    URL = pyqrcode.create(url)

    xbm = URL.xbm(scale=10)
    top = tkinter.Tk()
    bmp = tkinter.BitmapImage(data=xbm)
    
    bmp.config(background="white")
    
    label = tkinter.Label(image=bmp)
    label.pack()

    threading.Thread(target=hostit, args=(directory,)).start()
    
    top.mainloop()


    


if __name__ == "__main__":
    main()
