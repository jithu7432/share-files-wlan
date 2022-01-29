# Share-Files-Wlan
Host a file to your wireless network, so that others using the same network can download via a QR.

The code generates a QR code and a link, which you can share with others, or yourself.

I often use the `python -m http.server` to share files to my android device, since it was messy I created a QR code pop-up which directly leads to a file, if a file is hosted else, the working directory.

# Installation

Install the package

```bash
pip install .
```

Create an alias like this
```bash
alias serve='~/.local/venv/bin/python -m host.server'
```

And you can share the file via the terminal using the command line

```bash
serve myvideo.mkv
```

This will trigger a pop-up, and the link will appear on the terminal.

Scanning the QR will directly start downloading the files, I personally use this ad-free QR code scanner (android):

[QR Code & Bar-code Scanner](https://play.google.com/store/apps/details?id=com.scanteam.qrcodereader)

Don't forget to turn on the automatically open urls feature.

