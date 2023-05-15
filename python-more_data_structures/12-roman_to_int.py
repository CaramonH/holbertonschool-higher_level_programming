#!/usr/bin/pyton3
# Write a function that converts a Roman numeral to an integer


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_numerals = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M':1000}
    sum = 0
    for i in range(len(roman_string)):
