# Write two Python functions to find the minimum number in a list.
# The first function should compare each number to every other number on the list. 𝑂(𝑛2).
# The second function should be linear 𝑂(𝑛).

def func_1(my_list):
    """quadratic"""
    current_min = my_list[0]
    for i in my_list:
        is_smallest = True
        for j in my_list:
            if i > j:
                is_smallest = False
        if is_smallest == True:
            current_min = i
    return current_min

def func_2(my_list):
    """linear"""
    current_min = my_list[0]
    for i in my_list:
       if i < current_min:
           current_min = i
    return current_min

list = [4,1,16,0.3,44]
print(func_1(list))
print(func_2(list))