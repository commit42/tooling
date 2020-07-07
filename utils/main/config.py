import yaml

class Config:
    def __init__(self):
        with open(".c42/c42.yml", "r") as yml_file:
            self.config = yaml.load(yml_file, Loader=yaml.FullLoader)

    def get_config(self):
        return self.config

    def project_type(self):
        return self.config["project"]["type"]