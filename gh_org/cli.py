from os import getcwd
from os.path import isfile, expanduser, join
from argparse import ArgumentParser, ArgumentTypeError

CONFIG_DIR = join(expanduser('~'), '.gh_org')


def check_file(filename):
    if not isfile(filename):
        raise ArgumentTypeError("Config file: {0} does not exist".format(filename))
    return filename


def make_parser():
    parser = ArgumentParser(prog='gh_org',
                            description="Generate Terraform data for GitHub org user management")
    parser.add_argument('-c',
                        '--config-file',
                        metavar='FILE',
                        type=check_file,
                        default=join(CONFIG_DIR, 'config.ini'),
                        help="Config file")
    parser.add_argument('-o', '--output-dir',
                        default=getcwd(),
                        help="Output directory")

    return parser.parse_args()


def main():
    args = make_parser()
    print(args)
    pass
