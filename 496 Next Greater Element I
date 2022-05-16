def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    dict_2nd = {key: i for i, key in enumerate(nums2)}
    answer = []
    for each in range(len(nums1)):
        for j in range(dict_2nd[nums1[each]]+1, len(nums2)):  # величина в nums2
            if nums2[j] > nums1[each]:
                answer.append(nums2[j])
                break
        else:
            answer.append(-1)
    return answer


# tests
if __name__ == "__main__":
    test_n = 1
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    ans = [-1, 3, -1]
    assert nextGreaterElement(nums1, nums2) == ans, f"Wrong in test {test_n}, your answer is " \
                                                    f"{nextGreaterElement(nums1, nums2)}, "f"correct is {ans}"

    test_n += 1
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    ans = [3, -1]
    assert nextGreaterElement(nums1, nums2) == ans, f"Wrong in test {test_n}, your answer is " \
                                                    f"{nextGreaterElement(nums1, nums2)}, "f"correct is {ans}"
