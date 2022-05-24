def intToRoman(num: int):
    num_dict = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                }

    num = str(num)
    pointer = len(num)

    return roman


# test code
if __name__ == "__main__":
    answer_dict = {3: 'III',
                   58: 'LVIII',
                   1994: 'MCMXCIV',
                   14: 'XIV',
                   4: 'IV',
                   952: 'CMLII'}
    test_n = 1
    for i in answer_dict:
        intToRoman(i)
        assert intToRoman(i) == answer_dict[i], f"Wrong test {test_n}, your answer is {intToRoman(i)}, " \
                                                f"correct is {answer_dict[i]}"
        test_n += 1
