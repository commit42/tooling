#!/usr/bin/python3
import sys
import argparse
from utils.main.cli import Cli


avalaible_flags = {"guest": False, "partial": False}

cli_processor = Cli(sys.argv[1:], avalaible_flags)
cli_processor.run()