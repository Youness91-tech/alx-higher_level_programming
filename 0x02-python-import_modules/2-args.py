#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    arg_ctr = len(sys.argv)
    if arg_ctr == 1:
        print("0 arguments.")
    elif arg_ctr == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_ctr - 1))
    for i in range(1, arg_ctr):
        print("{}: {}".format(i, sys.argv[i]))
