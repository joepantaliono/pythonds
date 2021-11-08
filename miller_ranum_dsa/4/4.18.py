# palindrome checker
from deque import Deque

def pal_check(string):
    """check if a string reads the same forward and backward, ex. radar, civic, level"""
    pal_string = Deque()
    # populate with letters
    for char in string:
        pal_string.add_front(char)

    while pal_string.size() > 1:
        # take off each end, compare
        first = pal_string.remove_rear()
        second = pal_string.remove_front()
        if first != second:
            return False
    return True

pal_check("level") #true
pal_check("radar") #true
pal_check("lfasnfgklsjrng") #false
pal_check("98766789") #true