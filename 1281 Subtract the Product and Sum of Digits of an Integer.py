def subtractProductAndSum(n: int) -> int:
    """Given an integer number n, return the difference between the product of its digits and the sum of its digits."""
    n = str(n)
    product = 1
    summat = 0
    for each in n:
        product *= int(each)
        summat += int(each)
    return product - summat


n = 234
print(subtractProductAndSum(n))