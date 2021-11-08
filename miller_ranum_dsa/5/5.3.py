def recursive_sum(nums):
    """sum a list of integers using recursion"""
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + recursive_sum(nums[1:])
    

recursive_sum([3,4,3,34]) # 44