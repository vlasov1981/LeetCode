def romanToInt(s: str) -> int:
    """13. Roman to Integer
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Given a roman numeral, convert it to an integer"""
    num_dict = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                }
    answer = 0
    pointer = 0
    if len(s) == 1:
        return num_dict[s[pointer]]
    while pointer < len(s) - 1:
        if num_dict[s[pointer]] >= num_dict[s[pointer+1]]:
            answer += num_dict[s[pointer]]
        else:
            answer += -num_dict[s[pointer]]
        pointer += 1
    answer += num_dict[s[pointer]]
    return answer

# test code
if __name__ == "__main__":
    answer_dict = {'III': 3,
                   'LVIII': 58,
                   'MCMXCIV': 1994,
                   'XIV': 14,
                   'IV': 4,
                   'CMLII': 952}
    test_n = 1
    for i in answer_dict:
        romanToInt(i)
        assert romanToInt(i) == answer_dict[i], f"Wrong test {test_n}, your answer is {romanToInt(i)}, " \
                                                f"correct is {answer_dict[i]}"
        test_n += 1
