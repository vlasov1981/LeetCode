'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''


def mergeTwoLists(list1, list2):
    flag_1 = 0
    flag_2 = 0
    combined_list = []

    if len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1

    while flag_1 < len(list1) and flag_2 < len(list2):
        if list1[flag_1] <= list2[flag_2]:
            combined_list.append(list1[flag_1])
            flag_1 += 1
        else:
            combined_list.append(list2[flag_2])
            flag_2 += 1

    if flag_1 == len(list1):
        combined_list.append(*list2[flag_2:])
    else:
        combined_list.append(*list1[flag_1:])
    return combined_list


# tests
if __name__ == "__main__":
    test_n = 1

    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    ans = [1, 1, 2, 3, 4, 4]
    assert mergeTwoLists(list1, list2) == ans, f"Wrong in test {test_n}, your answer is " \
                                               f"{mergeTwoLists(list1, list2)}, correct is {ans}"


    test_n += 1
    list1 = []
    list2 = []
    ans = []
    assert mergeTwoLists(list1, list2) == ans, f"Wrong in test {test_n}, your answer is " \
                                               f"{mergeTwoLists(list1, list2)}, correct is {ans}"
    test_n += 1
    list1 = []
    list2 = [0]
    ans = [0]
    assert mergeTwoLists(list1, list2) == ans, f"Wrong in test {test_n}, your answer is " \
                                               f"{mergeTwoLists(list1, list2)}, correct is {ans}"
