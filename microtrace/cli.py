import sys
from .core import trace

HELP = """
MicroTrace v0.1

Usage:

python3 -m microtrace <host>

Example:

python3 -m microtrace google.com
"""


def main():
    args = sys.argv[1:]

    if not args:
        print(HELP)
        return

    trace(args[0])
