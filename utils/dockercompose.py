import subprocess


class DockerCompose:
    def build_command(self, command):
        subprocess.run(f"docker-compose run --rm {command}".split())

    def run(self):
        subprocess.run("docker-compose up -d".split())

    def composer(self, args):
        self.build_command(f"composer --ignore-platform-reqs {args}")

    def magerun(self, args):
        self.build_command(f"web n98-magerun {args}")

    def yarn(self, args):
        self.build_command(f"theme yarn {args}")
