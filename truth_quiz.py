questions = (
    (r'True and True'), # True
    (r'False and True'), # False
    (r'1 == 1 and 2 == 1'), # False
    (r'"test" == "test"'), # True
    (r'1 == 1 or 2 != 1'), # True
    (r'True and 1 == 1'), # True
    (r'False and 0 != 0'), # False
    (r'True or 1 == 1'), # True
    (r'False and 0 != 0'), # False
    (r'True or 1 == 1'), # True
    (r'"test" == "testing"'), # False
    (r'1 != 0 and 2 == 1'), # False
    (r'"test" != "testing"'), # True
    (r'"test" == 1'), # False
    (r'not (True and False)'), # True
    (r'not (1 == 1 and 0 != 1)'), # False
    (r'not (10 == 1 or 1000 == 1000)'), # False
    (r'not (1 != 10 or 3 == 4)'), # False
    (r'not ("testing" == "testing" and "Zed" == "Cool Guy")'), # True
    (r'1 == 1 and (not ("testing" == 1 or 1 == 0))'), # True
    (r'"chunky" == "bacon" and (not (3 == 4 or 3 == 3))'), # False
    (r'3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))') # False
    )

correct = []
for question in questions:
    print(f"{question}: True or False?")
    answer = input("> ")
    print(f"You wrote: {answer}")
    truth = str(eval(question))
    print(f"The answer was: {truth}")
    if truth.lower() == answer.lower():
        print("You were right!")
        correct.append("1")
    else:
        print("You were incorrect!")
        correct.append("0")
    print("---")
print("You got", correct.count("1"), "of", len(correct), "correct!")

