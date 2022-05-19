def mergeAlternately(word1: str, word2: str) -> str:
    output = ""
    difference = len(word1) - len(word2) # 0 - equal, + - 1st longer, - - third longer

    if difference == 0:
        for i in range(len(word1)):
            output += (word1[i] + word2[i])
    elif difference > 0:  # 1st word is longer
        for i in range(len(word2)):
            output = output + word1[i] + word2[i]
        output += word1[len(word2):]
    else:
        for i in range(len(word1)):
            output = output + word1[i] + word2[i]
        output += word2[len(word1):]

    return output


# tests
if __name__ == "__main__":
    test_n = 1
    word1 = "abc"
    word2 = "pqr"
    ans = "apbqcr"
    assert mergeAlternately(word1, word2) == ans, f"Wrong in test {test_n}, your answer is " \
                                                  f"{mergeAlternately(word1, word2)}, "f"correct is {ans}"

    test_n += 1
    word1 = "ab"
    word2 = "pqrs"
    ans = "apbqrs"
    assert mergeAlternately(word1, word2) == ans, f"Wrong in test {test_n}, your answer is " \
                                                  f"{mergeAlternately(word1, word2)}, "f"correct is {ans}"

    test_n += 1
    word1 = "abcd"
    word2 = "pq"
    ans = "apbqcd"
    assert mergeAlternately(word1, word2) == ans, f"Wrong in test {test_n}, your answer is " \
                                                  f"{mergeAlternately(word1, word2)}, "f"correct is {ans}"
