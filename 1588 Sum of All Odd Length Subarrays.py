def sumOddLengthSubarrays(arr: list[int]) -> int:
    """Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
    A subarray is a contiguous subsequence of the array.
    Return the sum of all odd-length subarrays of arr.
    """
    answer = 0
    left, right = 0, 1
    while left <= len(arr) - 1:
        while right <= len(arr):
            answer += sum(arr[left:right])
            right += 2
        left += 1
        right = left + 1
    return answer


# tests
if __name__ == "__main__":
    test_n = 1
    arr = [1, 4, 2, 5, 3]
    ans = 58
    assert sumOddLengthSubarrays(arr) == ans, f"Wrong in test {test_n}, your answer is " \
                                              f"{sumOddLengthSubarrays(arr)}, "f"correct is {ans}"

    test_n += 1
    arr = [1, 2]
    ans = 3
    assert sumOddLengthSubarrays(arr) == ans, f"Wrong in test {test_n}, your answer is " \
                                              f"{sumOddLengthSubarrays(arr)}, "f"correct is {ans}"

    test_n += 1
    arr = [10, 11, 12]
    ans = 66
    assert sumOddLengthSubarrays(arr) == ans, f"Wrong in test {test_n}, your answer is " \
                                              f"{sumOddLengthSubarrays(arr)}, "f"correct is {ans}"
