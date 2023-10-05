#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operators = ["+", "-", "*", "/"]
    if sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == operators[0]:
        print("{} {} {} = {}".format(a, sys.argv[2], b, add(a, b)))
    elif sys.argv[2] == operators[1]:
        print("{} {} {} = {}".format(a, sys.argv[2], b, sub(a, b)))
    elif sys.argv[2] == ooperators[2]:
        print("{} {} {} = {}".format(a, sys.argv[2], b, mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, sys.argv[2], b, div(a, b)))
