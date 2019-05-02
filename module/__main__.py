# -*- coding: utf-8 -*-
"""Main module.
"""
import argparse
from module import main as Module


def main() -> None:
    """Main function.
    Parse arguments and pass them to module.
    """
    parser = argparse.ArgumentParser(description='Pipenv simple skeleton.')
    parser.add_argument('foo', help='foo bar')
    args = parser.parse_args()

    Module.main(args.foo)


if __name__ == '__main__':
    main()
