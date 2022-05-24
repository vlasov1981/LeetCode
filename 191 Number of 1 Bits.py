def hammingWeight(n):
    n = list(bin(n)).count("1")
    return n
n = 10000000000000000000000000001011
print(hammingWeight(n))