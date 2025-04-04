#! /usr/bin/env python3

import sys

if __name__ == "__main__":
    if sys.version_info < (3, 13):
        print(f"Netra requires Python 3.13+\nYou are using Python {sys.version.split()[0]}, which is not supported.")
        sys.exit(1)

    from netra import netra
    netra.main()