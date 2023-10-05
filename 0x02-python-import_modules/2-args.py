#!/usr/bin/python3

import sys

arg_ctr = len(sys.argv) - 1
if arg_ctr == 0:
    print("0 arguments.")
elif arg_ctr == 1:
    print("1 argument:")
    print("1:", sys.argv[1])
else:
    print(arg_ctr, "arguments:")
    for i in range(1, arg_ctr + 1):
        print(i, ":", sys.argv[i])
