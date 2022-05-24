def findTheDifference(s: str, t: str) -> str:
    tmp_dict = {}
    for i in s:
        if i not in tmp_dict:
            tmp_dict[i] = 0
        tmp_dict[i] += 1

    for k in t:
        if k not in s:
            return k
        else:
            tmp_dict[k] -= 1
            if tmp_dict[k] < 0:
                return k






# tests
if __name__ == "__main__":
    test_n = 1
    s = "abcd"
    t = "abcde"
    ans = "e"
    assert findTheDifference(s, t) == ans, f"Wrong in test {test_n}, your answer is " \
                                      f"{findTheDifference(s, t)}, "f"correct is {ans}"

    test_n += 1
    s = ""
    t = "y"
    ans = "y"
    assert findTheDifference(s, t) == ans, f"Wrong in test {test_n}, your answer is " \
                                           f"{findTheDifference(s, t)}, "f"correct is {ans}"

    test_n += 1
    s = "a"
    t = "aa"
    ans = "a"
    assert findTheDifference(s, t) == ans, f"Wrong in test {test_n}, your answer is " \
                                           f"{findTheDifference(s, t)}, "f"correct is {ans}"

