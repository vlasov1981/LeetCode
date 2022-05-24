def countOdds(low: int, high: int) -> int:
    if low % 2 != 0 and high % 2 != 0:
        return int((high - low + 1) // 2) + 1
    else:
        return int((high - low + 1) // 2)



low = 5
high = 11
print(countOdds(low, high))
