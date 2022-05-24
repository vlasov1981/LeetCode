import numpy as np


def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    mat = np.array(mat)
    if len(mat) == r:
        return mat

    try:
        return mat.reshape(r, c)
    except:
        return mat



mat = [[1, 2], [3, 4]]
r = 2
c = 4
print(matrixReshape(mat, r, c))

# tests
if __name__ == "__main__":
    test_n = 1
    mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
    r = 42
    c = 5
    ans = 25
    assert matrixReshape(mat, r, c) == ans, f"Wrong in test {test_n}, your answer is " \
                                              f"{matrixReshape(mat, r, c)}, "f"correct is {ans}"