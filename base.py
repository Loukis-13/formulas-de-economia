#!/bin/python3

import argparse

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="",
    epilog="FORMULA: ",
)

parser.add_argument("", type=None, help="")

# parser.add_argument("", type=None, help="")
# parser.add_argument("", type=None, help="")
# parser.add_argument("", type=None, help="")
# parser.add_argument("", type=None, help="")

parser.add_argument("-n", type=int, default=4, help="Número de casas decimais")

args = parser.parse_args()

print(f"{ 1 :.{args.n}%}")
