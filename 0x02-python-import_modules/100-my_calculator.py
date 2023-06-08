#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":

    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    len_args = len(sys.argv)
    if len_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    result = operators[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
