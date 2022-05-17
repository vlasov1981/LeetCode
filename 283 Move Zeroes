def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count +=1
    for each in range(count, len(nums)):
        nums[each] = 0


    return nums





# tests
if __name__ == "__main__":
    test_n = 1
    nums = [0, 1, 0, 3, 12]
    ans = [1, 3, 12, 0, 0]

    assert moveZeroes(nums) == ans, f"Wrong in test {test_n}, your answer is " \
                                    f"{moveZeroes(nums)}, "f"correct is {ans}"

    test_n += 1
    nums = [0]
    ans = [0]

    assert moveZeroes(nums) == ans, f"Wrong in test {test_n}, your answer is " \
                                    f"{moveZeroes(nums)}, "f"correct is {ans}"
