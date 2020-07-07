import subprocess
import yaml
from .dockercompose import DockerCompose


class Magento:
    def __init__(self):
        with open(".c42/c42.yml", "r") as yml_file:
            self.config = yaml.load(yml_file, Loader=yaml.FullLoader)
        self.dockercompose_processor = DockerCompose()

    def update_base_url(self):
        base_url = self.config["magento"]["url"]
        self.dockercompose_processor.magerun(
            f"config:set web/unsecure/base_url https://{base_url}/")
        self.dockercompose_processor.magerun(
            f"config:set web/secure/base_url https://{base_url}/")

    def generate_local_xml(self):
        db = self.config["magento"]["db"]
        backoffice_path = self.config["magento"]["backoffice_path"]
        subprocess.run("rm htdocs/app/etc/local.xml".split())
        self.dockercompose_processor.magerun(
            f"local-config:generate db root root {db} files {backoffice_path} a0365f41e5bf39ab158608c5fef8d270")

    def clear_cache(self):
        self.dockercompose_processor.magerun("cache:flush")
        self.dockercompose_processor.magerun("cache:clean")

    def disable_cache(self):
        self.dockercompose_processor.magerun("cache:disable")

    def enable_symlinks(self):
        self.dockercompose_processor.magerun("dev:symlinks --global --on")

    def database_send_data(self):
        self.dockercompose_processor.db_tty(self.config["magento"]["db"])

    def database_exec_command(self, args):
        self.dockercompose_processor.db_exec(
            args, self.config["magento"]["db"])

    def create_default_admin_user(self):
        self.dockercompose_processor.magerun(
            "admin:user:create c42 c42 c42 c42 c42")
