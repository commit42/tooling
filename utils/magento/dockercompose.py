import subprocess


class DockerCompose:
    def build_command_run(self, command):
        subprocess.run(f"docker-compose run --rm {command}".split())

    def build_command_exec(self, container, command):
        tmp_command = f"docker-compose exec -T {container} bash -c".split()
        subprocess.run([*tmp_command, command])

    def build_command_exec_piped(self, container, command, stdout):
        tmp_command = f"docker-compose exec -T {container} bash -c".split()
        subprocess.run([*tmp_command, command], stdin=stdout)

    def run(self):
        subprocess.run("docker-compose up -d".split())

    def composer(self, args):
        self.build_command_run(f"composer --ignore-platform-reqs {args}")

    def magerun(self, args):
        self.build_command_run(f"web n98-magerun {args}")

    def yarn(self, args):
        self.build_command_run(f"theme yarn {args}")

    def db_tty(self, db_name):
        self.build_command_exec("db", f"mysql -uroot -proot {db_name}")

    def db_exec(self, args, db_name):
        echo_command = subprocess.Popen(
            f"echo {args}".split(), stdout=subprocess.PIPE)

        self.build_command_exec_piped(
            "db", f"mysql -uroot -proot {db_name}", echo_command.stdout)
