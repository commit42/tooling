import subprocess
from pathlib import Path

print("## Start internal tool installation ##")

print("Create folder named .c42 in home directory")

home = str(Path.home())
files_full_path = f"{home}/.c42"
subprocess.run(f"mkdir {files_full_path}".split())

print("Chmoding file to be executable")
subprocess.run("chmod +x c42.py".split())

print("Copy required files to .c42 previously creted folder")

subprocess.run(f"cp -R ./utils {files_full_path}".split())
subprocess.run(f"cp ./c42.py {files_full_path}".split())


print("Create symlink to add c42 to bin path")

subprocess.run(f"sudo ln -s {files_full_path}/c42.py /usr/local/bin/c42".split())


