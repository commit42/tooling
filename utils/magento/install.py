import subprocess
import os.path
from os import path
from .download import Download
from .importer import Importer
from .dockercompose import DockerCompose
from .magento import Magento


class Install:
    def __init__(self, flags):
        self.download_processor = Download()
        self.importer_processor = Importer()
        self.dockercompose_processor = DockerCompose()
        self.magento = Magento()
        self.is_guest = flags["guest"]
        self.partial = flags["partial"]

    def run(self):
        print("Start project installation")

        if not path.exists("docker-compose.yml"):
            subprocess.run("pwd")
            print("Move docker-compose file")

            dc_file_name = "docker-compose.yml.guest.dist" if self.is_guest else "docker-compose.yml.dist"
            subprocess.run(
                f"cp .c42/{dc_file_name} docker-compose.yml".split())

        if not path.exists(".c42/docker/entrypoint.sh"):
            print("Move entrypoint file")
            subprocess.run(
                "cp .c42/docker/entrypoint.sh.dist .c42/docker/entrypoint.sh".split())

        if not self.partial:
            print("Download project database...")
            self.download_processor.database()

        if not self.partial:
            print("Import project database...")
            self.importer_processor.database()

        if not self.partial:
            print("Import project media...")
            self.download_processor.media()

        print("Run composer install")
        self.dockercompose_processor.composer("install")

        print("Run theme install")
        self.dockercompose_processor.yarn("")

        print("Up all docker containers")
        self.dockercompose_processor.run()

        print("Set up local.xml")
        self.magento.generate_local_xml()

        print("Update base url")
        self.magento.update_base_url()

        print("Create default admin user")
        self.magento.create_default_admin_user()

        print("Clear cache")
        self.magento.clear_cache()

        print("Enable symlinks")
        self.magento.enable_symlinks()

        print("Chmod var and media")
        subprocess.run("sudo chmod -R 777 htdocs/var".split())
        subprocess.run("sudo chmod -R 777 htdocs/media".split())
