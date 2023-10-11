#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ttl = 0
    for v in range(len(roman_string)):
        if v > 0 and roman[roman_string[v]] > roman[roman_string[v - 1]]:
            ttl += roman[roman_string[v]] - 2 * roman[roman_string[v - 1]]
        else:
            ttl += roman[roman_string[v]]
    return ttl
