import itertools

def numOfSubarrays( arr: list[int]) -> int:
    """
    Given an array of integers arr, return the number of subarrays with an odd sum.
    Since the answer can be very large, return it modulo 109 + 7
    """
    arr_s = len([sum(arr[i:j]) for i, j in itertools.combinations(range(len(arr)+1), 2) if sum(arr[i:j]) % 2 != 0])
    # odd_sum = [sum(i) for i in arr_s if sum(i) % 2 != 0]
    # print(arr_s)
    return arr_s%(10**9+7)







arr = [1,3,5]
print(numOfSubarrays(arr))