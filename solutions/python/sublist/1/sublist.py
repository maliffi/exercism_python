"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 3
SUPERLIST = 2
EQUAL = 1
UNEQUAL = 4


def sublist(list_one, list_two):
    str_one = ', '.join(map(str, list_one))
    str_two = ', '.join(map(str, list_two))
    print(f"str_one:{str_one}, str_two:{str_two}")
    if str_one == str_two:
        return EQUAL
    try:
        if len(list_two) < len(list_one):
            print("list two is shorter")
            if str_two == "" or str_one.index(str_two) >=0:
                return SUPERLIST
        elif len(list_two) > len(list_one):
            print("list one is shorter")
            if str_one == "" or str_two.index(str_one) >=0:
                return SUBLIST
    except ValueError:
        return UNEQUAL
    return UNEQUAL