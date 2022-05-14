def longestCommonPrefix(strs: list[str]) -> str:
    output = ""
    strs.sort()
    n1 = len(strs[0])
    n2 = len(strs[-1])

    i = 0
    j = 0
    while i < n1 and j < n2:
        if strs[0][i] == strs[-1][j]:
            output += strs[0][i]
        else:
            return output
        i += 1
        j += 1
    return output


if __name__ == "__main__":
    test_n = 1
    strs = ["flower", "flow", "flight"]
    ans = "fl"
    assert longestCommonPrefix(strs) == ans, f"Wrong in test {test_n}, your answer is " \
                                             f"{longestCommonPrefix(strs)}, "f"correct is {ans}"
    test_n += 1

    strs = ["dog", "racecar", "car"]
    ans = ""
    assert longestCommonPrefix(strs) == ans, f"Wrong in test {test_n}, your answer is " \
                                             f"{longestCommonPrefix(strs)}, "f"correct is {ans}"
    test_n += 1
