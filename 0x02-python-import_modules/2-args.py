#!/usr/bin/python3
import sys

if __name__ == "__main__":
    len_args = len(sys.argv) - 1
    if len_args == 0:
        print("{} arguments.".format(len_args))
    else:
        print("{} argument{}:".format(len_args, "s" if len_args > 1 else ""))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
