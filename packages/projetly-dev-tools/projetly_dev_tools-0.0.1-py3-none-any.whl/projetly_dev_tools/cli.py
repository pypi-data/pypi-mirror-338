"""
The command-line interface for the downloader
"""
import argparse
from .projetly_dev_tools import projetly_plugins


def main():
    parser = argparse.ArgumentParser(
        description="Tool used by developers to assist in managing projetly packages."
    )
    parser.add_argument(
        "module", type=str,
        help="The module used."
    )
    parser.add_argument(
        "subcommand", type=str,
        help="The subcommand used."
    )
    parser.add_argument(
        "name", type=str,
        help="The name used."
    )
    # parser.add_argument(
    #     "--output", "-o",
    #     help=("Destination local file path. If not set, the resource "
    #             "will be downloaded to the current working directory, with filename "
    #             "same as the basename of the URL")
    # )
    args = parser.parse_args()
    projetly_plugins(args.module, args.subcommand, args.name)
    # print("Download successful! (size: {} B)".format(file_size))

if __name__ == "__main__":
    main()