import numpy as np


def diagonalSum(mat: list[list[int]]) -> int:
    mat = np.array(mat)
    if len(mat) == 1:
        return mat[0][0]
    d1 = np.diag(mat)
    d2 = np.diag(np.fliplr(mat))
    n = len(d1)

    if n % 2 != 0:
        answer = sum(d1) + sum(d2) - d1[n // 2]
    else:
        answer = sum(d1) + sum(d2)
    return answer


# tests
if __name__ == "__main__":
    test_n = 1
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    ans = 25
    assert diagonalSum(mat) == ans, f"Wrong in test {test_n}, your answer is " \
                                              f"{diagonalSum(mat)}, "f"correct is {ans}"

    test_n += 1
    mat = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]
    ans = 8
    assert diagonalSum(mat) == ans, f"Wrong in test {test_n}, your answer is " \
                                    f"{diagonalSum(mat)}, "f"correct is {ans}"

    test_n += 1
    mat = [[5]]
    ans = 5
    assert diagonalSum(mat) == ans, f"Wrong in test {test_n}, your answer is " \
                                    f"{diagonalSum(mat)}, "f"correct is {ans}"
