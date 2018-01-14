# encoding: utf-8


def p_game_description():
    """
    Output game description
    :return: None
    """
    print("Guess the correct numbers in as few times as possible\n"
          "rule:\n"
          "A total of four digits\n"
          "Numbers do not repeat\n"
          "Range: 0 ~ 9\n"
          "Each input gives you two feedback. \n"
          "The first number means that the X numbers are both correct in number and position. \n"
          "The second number means that the Y numbers are correct in numbers and incorrect in position.\n"
          "According to this clue, keep getting close to the correct answer.\n"
          "And some luck ^-^\n")


def game_main():
    # name = raw_input("What is your name?") #only on python 2.x
    user_input = input("Game Start, Please input your answer:")
    print("Hello " + user_input)


if __name__ == '__main__':
    print()
    pass
else:
    print(__name__)
    pass

