def largestPerimeter(nums: list[int]) -> int:
    """Given an integer array nums, return the largest perimeter of a triangle with a non-zero area,
    formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0."""
    if len(nums) < 3:  # check if array is too short
        return 0
    nums.sort(reverse=True)
    left = 0
    right_1 = 1
    right_2 = 2
    while right_2 <= len(nums) - 1:
        if nums[left] >= nums[right_1] + nums[right_2]:
            left += 1
            right_1 += 1
            right_2 += 1
        else:
            return sum(nums[left: right_2 + 1])
    return 0


# test code
if __name__ == "__main__":
    test_n = 1
    nums = [2, 1, 2]
    ans = 5
    assert largestPerimeter(nums) == ans, f"Wrong in test {test_n}, your answer is {largestPerimeter(nums)}, " \
                                          f"correct is {ans}"
    test_n += 1

    nums = [1, 2, 1]
    ans = 0
    assert largestPerimeter(nums) == ans, f"Wrong in test {test_n}, your answer is {largestPerimeter(nums)}, " \
                                          f"correct is {ans}"
    test_n += 1

    nums = [3, 6, 2, 3]  # 6,3,3,2
    ans = 8
    assert largestPerimeter(nums) == ans, f"Wrong in test {test_n}, your answer is {largestPerimeter(nums)}, " \
                                          f"correct is {ans}"
    test_n += 1

    # 4
    nums = [1, 2, 2, 4, 18, 8]  # 18 8 4 2 2 1
    ans = 5
    assert largestPerimeter(nums) == ans, f"Wrong in test {test_n}, your answer is {largestPerimeter(nums)}, " \
                                          f"correct is {ans}"
    test_n += 1
