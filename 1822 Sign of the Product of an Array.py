def arraySign(nums: list[int]) -> int:
    """
    There is a function signFunc(x) that returns:
    1 if x is positive.
    -1 if x is negative.
    0 if x is equal to 0.
    You are given an integer array nums. Let product be the product of all values in the array nums.

    Return signFunc(product).
    """
    negative_counter = 0
    for each in nums:
        if each == 0:
            return 0
        elif each < 0:
            negative_counter += 1
    if negative_counter % 2 == 0:
        return 1
    return -1




# tests
if __name__=="__main__":
    test_n = 1
    nums = [-1, -2, -3, -4, 3, 2, 1]
    ans = 1
    assert arraySign(nums) == ans , f"Wrong in test {test_n}, your answer is " \
                                             f"{arraySign(nums)}, "f"correct is {ans}"
    test_n += 1
    nums = [1,5,0,2,-3]
    ans = 0
    assert arraySign(nums) == ans, f"Wrong in test {test_n}, your answer is " \
                                   f"{arraySign(nums)}, "f"correct is {ans}"
    test_n += 1
    nums = [-1,1,-1,1,-1]
    ans = -1
    assert arraySign(nums) == ans, f"Wrong in test {test_n}, your answer is " \
                                   f"{arraySign(nums)}, "f"correct is {ans}"
    test_n += 1