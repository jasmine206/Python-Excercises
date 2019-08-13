"""
Given
A list, a tuple and a set of numbers:

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = (3, 4, 1, 2, 7, 6, 5, 8)
c = {5, 6, 7, 8, 1, 2, 3, 4}

Then
Decide if a, b, c contain the same set of numbers.

Expected output
The result should be true.
"""

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = (3, 4, 1, 2, 7, 6, 5, 8)
c = {5, 6, 7, 8, 1, 2, 4, 4, 4}


"""
Set does not allow duplicate members. 
Solution is checking if both list and tuple have all members of set by using `for` loop
"""


def same_set_of_number(my_list, my_tuple, my_set):
    if len(my_set) != len(my_tuple) or len(my_list) != len(my_set):
        return False
    else:
        for item in my_set:
            if item not in my_list or item not in my_tuple:
                return False
        return True


print(a)
print(b)
print(c)

print('\nDo these list, tuple and set above contain the same set of number?')
print(same_set_of_number(a, b, c))
