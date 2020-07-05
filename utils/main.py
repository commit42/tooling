
from .install import Install
from .dockercompose import DockerCompose


class Main:
    def __init__(self, main_param, args, flags):
        if main_param == "install":
            install_process = Install(flags)
            install_process.run()
        elif main_param == "magerun":
            dockercompose_process = DockerCompose()
            dockercompose_process.magerun(" ".join(args))
        elif main_param == "composer":
            dockercompose_process = DockerCompose()
            dockercompose_process.composer(" ".join(args))
