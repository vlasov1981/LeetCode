def twoSum( nums: list[int], target: int):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add
    up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    """

    temp_dict = {}
    index_counter = -1
    for i in nums:
        index_counter += 1
        if i in temp_dict:
            return [index_counter, temp_dict[i]]
        else:
            temp_dict[target-i] = index_counter



nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
