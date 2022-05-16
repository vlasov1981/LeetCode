def isValid(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string
    is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    """
    if len(s) % 2 != 0:
        return False

    stack = []
    parentheses_dict = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    for each in s:
        if each in parentheses_dict:
            stack.append(parentheses_dict[each])
        else:
            if len(stack) != 0 and each == stack[-1]:
                del stack[-1]
            else:
                return False
    if len(stack) == 0:
        return True
    return False



# tests
if __name__ == "__main__":
    test_n = 1
    s = "()"
    ans = True
    assert isValid(s) == ans, f"Wrong in test {test_n}, your answer is " \
                              f"{isValid(s)}, "f"correct is {ans}"

    test_n += 1
    s = "()[]{}"
    ans = True
    assert isValid(s) == ans, f"Wrong in test {test_n}, your answer is " \
                              f"{isValid(s)}, "f"correct is {ans}"

    test_n += 1
    s = "(]"
    ans = False
    assert isValid(s) == ans, f"Wrong in test {test_n}, your answer is " \
                              f"{isValid(s)}, "f"correct is {ans}"

    test_n += 1
    s = "((])"
    ans = False
    assert isValid(s) == ans, f"Wrong in test {test_n}, your answer is " \
                              f"{isValid(s)}, "f"correct is {ans}"

    test_n += 1
    s = "){"
    ans = False
    assert isValid(s) == ans, f"Wrong in test {test_n}, your answer is " \
                              f"{isValid(s)}, "f"correct is {ans}"
