# encoding: utf-8
import random

def game_introduction():
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
    """
    The overall framework of the game structure.
    :return:
    """
    num_answer = 0

    def init_answer():
        num_answer = ''.join([str(i) for i in random.sample(range(0, 9), 4)])
        pass

    def game_start():
        init_answer()
        user_input = input("Game Start, Please input your answer:")
        pass

    def game_run():
        pass

    def game_over():
        pass

    # name = raw_input("What is your name?") #only on python 2.x
    while 1:
        game_start()
        game_run()
        game_over()


if __name__ == '__main__':
    game_introduction()
    game_main()
    pass
else:
    print("%s", __name__)
    pass
