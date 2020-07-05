import sys


class Cli:
    def __init__(self, args, avalaible_flags):
        if len(args) > 0:
            self.args = args[1:]
            self.main_param = args[0]
            self.avalaible_flags = avalaible_flags
        else:
            self.help()
            sys.exit()

    def parse_args(self):
        clean_args = []

        for arg in self.args:
            if "--" in arg:
                self.avalaible_flags[arg[2:]] = True
            else:
                clean_args.append(arg)

        return [clean_args, self.avalaible_flags]

    def help(self):
        print("""Avalaible arguments :
            install [--guest, --partial]
            magerun [args]
            composer [args]
        """)
