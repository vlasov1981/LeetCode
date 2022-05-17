def checkStraightLine(coordinates: list[list[int]]) -> bool:
    if len(coordinates) == 2:
        return True
    counter = 0
    for i in range(1,len(coordinates)):
        if coordinates[i][0] == coordinates[i-1][0]:
            counter += 1
    if counter == len(coordinates) - 1:
        return True

    def eq_solution(x1, y1, x2, y2):
        if x1 != x2:
            k = (y1 - y2) / (x1 - x2)
        else:
            k = 0
        b = y1 - k * x1
        return [k, b]

    x1 = coordinates[0][0]
    y1 = coordinates[0][1]
    x2 = coordinates[1][0]
    y2 = coordinates[1][1]
    # print(x1, x2, y1, y2)

    k = eq_solution(x1, y1, x2, y2)[0]
    b = eq_solution(x1, y1, x2, y2)[1]
    # print(k,b)

    for i in range(2, len(coordinates)):
        if coordinates[i][1] != k * coordinates[i][0] + b:
            return False
    return True


# tests
if __name__ == "__main__":
    test_n = 1
    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    ans = True
    assert checkStraightLine(coordinates) == ans, f"Wrong in test {test_n}, your answer is " \
                                                  f"{checkStraightLine(coordinates)}, "f"correct is {ans}"

    test_n += 1
    coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
    ans = False
    assert checkStraightLine(coordinates) == ans, f"Wrong in test {test_n}, your answer is " \
                                                  f"{checkStraightLine(coordinates)}, "f"correct is {ans}"

    test_n += 1
    coordinates = [[0, 0], [0, 1], [0, -1]]
    ans = True
    assert checkStraightLine(coordinates) == ans, f"Wrong in test {test_n}, your answer is " \
                                                  f"{checkStraightLine(coordinates)}, "f"correct is {ans}"
    test_n += 1
    coordinates = [[2, 4], [2, 5], [2, 8]]
    ans = True
    assert checkStraightLine(coordinates) == ans, f"Wrong in test {test_n}, your answer is " \
                                                  f"{checkStraightLine(coordinates)}, "f"correct is {ans}"
