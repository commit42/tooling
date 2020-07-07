import sys
from .config import Config
from utils.magento.main import Main as MagentoMain

class Cli:
    def __init__(self, args, avalaible_flags):

        self.submodule = self.load_sub_modules()

        if len(args) > 0:
            self.args = args[1:]
            self.main_param = args[0]
            self.avalaible_flags = avalaible_flags
        else:
            self.submodule.help()
            sys.exit()

    def run(self):
        parsed_args = self.parse_args()
        args = parsed_args[0]
        flags = parsed_args[1]

        self.submodule.run(self.main_param, args, flags)


    def parse_args(self):
        clean_args = []

        for arg in self.args:
            if "--" in arg:
                self.avalaible_flags[arg[2:]] = True
            else:
                clean_args.append(arg)

        return [clean_args, self.avalaible_flags]



    def load_sub_modules(self):
        config_processor = Config()

        avalaible_modules = {
            "magento": MagentoMain()
        }

        return avalaible_modules.get(config_processor.project_type(), "Error")