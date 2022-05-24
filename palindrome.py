def isPalindrome(x: int):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.
    For example, 121 is a palindrome while 123 is not.
    """
    x = str(x)
    n = len(x)
    left, right = 0, n - 1
    while left < right:
        if x[left] == x[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


x = -121
print(isPalindrome(x))