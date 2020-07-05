# c42 Internal tooling

To run package build use pyinstaller
python 3.6 or higher required

first run:

    pip install pyinstaller or pip3 install pyinstaller

then run:

    pyinstaller -F c42.py --distpath dist/{distrib_name}

mv dist/{distrib_name}/c42 /usr/local/bin/c42
