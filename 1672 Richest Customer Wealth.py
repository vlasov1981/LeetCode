def maximumWealth(accounts: list[list[int]]) -> int:
    """You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the
    i​​​​​​​​​​​th​​​​ customer has in the
    j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer
    has.
    A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer
    that has the maximum wealth."""

    return max([sum(i) for i in accounts])

# tests
if __name__ == "__main__":
    test_n = 1
    accounts = [[1,2,3],[3,2,1]]
    ans = 6
    assert maximumWealth(accounts) == ans, f"Wrong in test {test_n}, your answer is " \
                                              f"{maximumWealth(accounts)}, "f"correct is {ans}"

    test_n += 1
    accounts = [[1,5],[7,3],[3,5]]
    ans = 10
    assert maximumWealth(accounts) == ans, f"Wrong in test {test_n}, your answer is " \
                                           f"{maximumWealth(accounts)}, "f"correct is {ans}"

    test_n += 1
    accounts = [[2,8,7],[7,1,3],[1,9,5]]
    ans = 17
    assert maximumWealth(accounts) == ans, f"Wrong in test {test_n}, your answer is " \
                                           f"{maximumWealth(accounts)}, "f"correct is {ans}"