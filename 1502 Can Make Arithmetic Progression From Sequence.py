def canMakeArithmeticProgression(arr: list[int]) -> bool:
    if len(arr) >= 2:
        arr.sort()
    else:
        return False

    difference = arr[1] - arr[0]
    for i in range(1, len(arr)):
        if difference != arr[i] - arr[i-1]:
            return False
    return True


# tests
if __name__ == "__main__":
    test_n = 1
    arr = [3, 5, 1]
    ans = True
    assert canMakeArithmeticProgression(arr) == ans, f"Wrong in test {test_n}, your answer is " \
                                   f"{canMakeArithmeticProgression(arr)}, "f"correct is {ans}"
    test_n += 1

    arr = [1,2,4]
    ans = False
    assert canMakeArithmeticProgression(arr) == ans, f"Wrong in test {test_n}, your answer is " \
                                                     f"{canMakeArithmeticProgression(arr)}, "f"correct is {ans}"
    test_n += 1

