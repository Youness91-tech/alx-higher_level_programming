#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    num_args = len(sys.argv)
    if num_args == 1:
        print("0 arguments.")
    elif num_args == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args - 1))
    for i in range(1, num_args):
        print("{}: {}".format(i, sys.argv[i]))
