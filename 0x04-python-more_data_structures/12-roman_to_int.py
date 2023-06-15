#!/usr/bin/python3

def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [data[x] for x in roman_string] + [0]
    count = 0

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i+1]:
            count += numbers[i]
        else:
            count -= numbers[i]
    return count
