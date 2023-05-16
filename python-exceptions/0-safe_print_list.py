#!/usr/bin/python3
# Write a function that prints x elements of a list

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            print(element, end=' ')
            count += 1
            if count == x:
                break
        else:
            print()
        return count
    except TypeError:
        print("An error occurred while printing the list.")
        return count
