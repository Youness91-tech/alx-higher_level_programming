#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for value in range(len(roman_string)):
        if value > 0 and roman_values[roman_string[value]] > roman_values[roman_string[value - 1]]:
            total += roman_values[roman_string[value]] - 2 * roman_values[roman_string[value - 1]]
        else:
            total += roman_values[roman_string[value]]
    return total
