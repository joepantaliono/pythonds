def MergeSort(arr):
    # base case, can't divide any further
    if len(arr) <= 1:
        return arr

    # get mid, recursively split arr
    midpoint = len(arr) // 2
    left = MergeSort(arr[:midpoint])
    right = MergeSort(arr[midpoint:])

    # this will return the sorted list
    return merge(left, right)


def merge(left, right):
    """use two pointers to compare the elements in subarrays, appending
    the smaller element each time"""
    res = []
    left_pointer = 0
    right_pointer = 0

    # while there are elements in both arrays
    while left_pointer < len(left) and right_pointer < len(right):
        # append smaller one to res
        if left[left_pointer] < right[right_pointer]:
            res.append(left[left_pointer])
            left_pointer += 1
        else:
            res.append(right[right_pointer])
            right_pointer += 1

    # if while loop does not execute, we know there are either
    # elements in the left array or right array
    # so we can extend those elements
    res.extend(left[left_pointer:])
    res.extend(right[right_pointer:])
    return res


array = [7, 6, 5, 4, 3, 2, 1]
print(array)
result = MergeSort(array)
print(result)
