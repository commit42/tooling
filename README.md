# c42 Internal tooling

To run package build use nuitka

first run:

    pip install nuitka or pip3 install nuitka

then run:

    python3 -mnuitka --follow-imports --standalone c42.py

sudo mkdir -p /usr/local/c42

sudo cp -R c42.dist/ /usr/local/c42

ln /usr/local/c42/c42 /usr/local/bin/c42
