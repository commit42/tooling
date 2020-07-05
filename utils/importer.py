import yaml
import subprocess


class Importer:
    def __init__(self):
        with open(".c42/c42.yml", "r") as yml_file:
            self.config = yaml.load(yml_file, Loader=yaml.FullLoader)

    def database(self):
        magento_config_db = self.config["magento"]["db"]

        # @todo: add check if file exists
        if magento_config_db:
            print("## Run import database ##")

            subprocess.run("docker-compose up -d db".split())

            cat_command = subprocess.Popen(
                "xzcat .c42/tmp/dump.sql.xz".split(), stdout=subprocess.PIPE)
            subprocess.run(
                ["docker-compose", "exec", "-T", "db", "bash", "-c",
                    f"mysql -uroot -proot {magento_config_db}"],
                stdin=cat_command.stdout)
            print("Import complete")
