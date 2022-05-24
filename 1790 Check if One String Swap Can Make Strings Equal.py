def areAlmostEqual(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    temp1 = []
    temp2 = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            temp1.append(s1[i])
            temp2.append(s2[i])
            if len(temp1) > 2:
                return False
    temp1.sort()
    temp2.sort()
    if temp1 == temp2:
        return True
    return False

# tests
if __name__ == "__main__":
    test_n = 1
    s1 = "bank"
    s2 = "kanb"
    ans = True
    assert areAlmostEqual(s1, s2) == ans, f"Wrong in test {test_n}, your answer is " \
                              f"{areAlmostEqual(s1, s2)}, "f"correct is {ans}"

    test_n += 1
    s1 = "attack"
    s2 = "defend"
    ans = False
    assert areAlmostEqual(s1, s2) == ans, f"Wrong in test {test_n}, your answer is " \
                                          f"{areAlmostEqual(s1, s2)}, "f"correct is {ans}"

    test_n += 1
    s1 = "kelb"
    s2 = "kelb"
    ans = True
    assert areAlmostEqual(s1, s2) == ans, f"Wrong in test {test_n}, your answer is " \
                                          f"{areAlmostEqual(s1, s2)}, "f"correct is {ans}"

    test_n += 1
    s1 = "abcd"
    s2 = "dcba"
    ans = False
    assert areAlmostEqual(s1, s2) == ans, f"Wrong in test {test_n}, your answer is " \
                                          f"{areAlmostEqual(s1, s2)}, "f"correct is {ans}"