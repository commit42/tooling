import yaml
from .install import Install
from .dockercompose import DockerCompose
from .magento import Magento

class Main:
    def __init__(self):
        with open(".c42/c42.yml", "r") as yml_file:
            self.config = yaml.load(yml_file, Loader=yaml.FullLoader)
        self.dockercompose_processor = DockerCompose()

    def run(self, main_param, args, flags):
        if main_param == "install":
            install_process = Install(flags)
            install_process.run()
        elif main_param == "magerun":
            dockercompose_process = DockerCompose()
            dockercompose_process.magerun(" ".join(args))
        elif main_param == "composer":
            dockercompose_process = DockerCompose()
            dockercompose_process.composer(" ".join(args))
        elif main_param == "magento:mysql:tty":
            magento_process = Magento()
            magento_process.database_send_data()
        elif main_param == "magento:mysql":
            magento_process = Magento()
            magento_process.database_exec_command(" ".join(args))

    def help(self):
        print("""Avalaible arguments :
            install [--guest, --partial]
            magerun [args]
            composer [args]
            magento:mysql:tty => Example: "stdout | magento:mysql:tty"
            magento:mysql [args]
        """)