#!/usr/bin/python3
import sys

if __name__ == "__main__":
    result = 0
    for num in sys.argv[1:]:
        result += int(num)
    print(result)
