#!/usr/bin/python3
for ch in range(122, 96, -1):
    print("{:c}".format(ch - 32) if ch % 2 != 0 else "{:c}".format(ch), end="")
