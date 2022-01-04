# Share-Files-Wlan
Host a file to your wireless network, so that others using the same network can download.

The code generates a QR code and a link, which you can share with others, or yourself.

I often use the `python -m http.server` to share files to my android device, since it was messy I created a QR code pop-up which directly leads to a file, if a file is hosted else, the working directory.

# Installation

I use Python from a virtual environment by default, hence I have copied it to the `site-packages` so that I can use it as a module.

Create an alias like this
```bash
alias serve='~/.local/venv/bin/python -m host.server'
```

And you can share the file via the terminal using the command line

```bash
serve myvideo.mkv
```

This will trigger a pop-up, and the link will appear on the terminal.

Keep the `host` folder in the site packages, for eg:
```bash
/home/jithin/.local/venv/lib64/python3.10/site-packages/host
```

Scanning the QR will directly start downloading the files, I personally use this ad-free QR code scanner (android):

[QR Code & Barcode Scanner](https://play.google.com/store/apps/details?id=com.scanteam.qrcodereader)

Don't forget to turn on the automatically open URLS feature.
