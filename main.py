from chatcontrolapi.cli import classes
from chatcontrolapi import Logger
import logging
import argparse


if __name__ == "__main__":

    log = Logger('chatcontrolapi', level=logging.DEBUG)
    logging.getLogger('requests').setLevel(logging.ERROR)
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    commands =  dict(map(lambda cls: (cls.name, cls(subparsers, log)), classes))

    args = parser.parse_args()
    cmd = commands[args.command]

    cmd.main(args)
