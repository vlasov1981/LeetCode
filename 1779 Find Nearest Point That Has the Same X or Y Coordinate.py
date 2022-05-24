import math


def nearestValidPoint( x: int, y: int, points: list[list[int]]) -> int:
    distancies_dict = {}  # {index : distance}
    index_count = 0
    for each in points:
        if each[0] == x or each[1] == y:
            manh_distance = abs(x - each[0]) + abs(y - each[1])
            distancies_dict[index_count] = manh_distance
        index_count += 1

    min_distance = math.inf
    out_index = -1
    for key, value in distancies_dict.items():
        if value < min_distance:
            min_distance = value
            out_index = key

    return out_index



if __name__ == "__main__":
    test_n = 1
    x = 3
    y = 4
    points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
    ans = 2
    assert nearestValidPoint( x, y, points) == ans, f"Wrong in test {test_n}, your answer is " \
                                                    f"{nearestValidPoint( x, y, points)}, "f"correct is {ans}"
    test_n += 1

    x = 3
    y = 4
    points = [[3,4]]
    ans = 0
    assert nearestValidPoint(x, y, points) == ans, f"Wrong in test {test_n}, your answer is " \
                                                   f"{nearestValidPoint(x, y, points)}, "f"correct is {ans}"
    test_n += 1

    x = 3
    y = 4
    points =  [[2,3]]
    ans = -1
    assert nearestValidPoint(x, y, points) == ans, f"Wrong in test {test_n}, your answer is " \
                                                   f"{nearestValidPoint(x, y, points)}, "f"correct is {ans}"
    test_n += 1

