import yaml
import subprocess
from datetime import date


class Download:
    def __init__(self):
        with open(".c42/c42.yml", "r") as yml_file:
            self.config = yaml.load(yml_file, Loader=yaml.FullLoader)

    def database(self):
        remote_config = self.config["remote"]
        host = remote_config["host"]
        dump = remote_config["dump"]
        dump_path = remote_config["dump_path"]

        if host and dump:
            current_date = date.today().strftime("%Y-%m-%d")
            subprocess.run(
                f"rsync -avz {host}:{dump_path}/{current_date}/{dump} .c42/tmp/dump.sql.xz".split())
            print("Download complete")

    # def media(self):
