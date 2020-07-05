import sys
import argparse
from utils.main import Main
from utils.cli import Cli


avalaible_flags = {"guest": False, "partial": False}

cli_processor = Cli(sys.argv[1:], avalaible_flags)
args_and_flags = cli_processor.parse_args()

args = args_and_flags[0]
flags = args_and_flags[1]
main_param = sys.argv[1]

Main(main_param, args, flags)
