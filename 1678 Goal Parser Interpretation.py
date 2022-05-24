def interpret(command: str) -> str:
    command = command.replace("()", "o").replace("(al)", "al")
    return command


# tests
if __name__ == "__main__":
    test_n = 1
    command = "G()(al)"
    ans = "Goal"
    assert interpret(command) == ans, f"Wrong in test {test_n}, your answer is " \
                                      f"{interpret(command)}, "f"correct is {ans}"

    test_n += 1
    command = "G()()()()(al)"
    ans = "Gooooal"
    assert interpret(command) == ans, f"Wrong in test {test_n}, your answer is " \
                                      f"{interpret(command)}, "f"correct is {ans}"

    test_n += 1
    command = "(al)G(al)()()G"
    ans = "alGalooG"
    assert interpret(command) == ans, f"Wrong in test {test_n}, your answer is " \
                                      f"{interpret(command)}, "f"correct is {ans}"
