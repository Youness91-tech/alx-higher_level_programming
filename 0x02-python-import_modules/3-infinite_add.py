#!/usr/bin/python3

import sys
if __name__ == "__main__":
    total_sum = 0
    num_args = len(sys.argv)
    if num_args == 1:
        print("0")
    else:
        for i in range(1, num_args):
            total_sum += int(sys.argv[i])
        print(total_sum)
