import random

# the game riddle number, enjoy about this
def riddleGame():
    get_number = random.randrange(1, 10, 1)
    button = True
    welcome = " Welcome to te game, play with me ".center(50, '#')
    end = "thanks for you time, end of game"
    while button:
        print(welcome.center(50, '#'))

        try:
            get_user: int = int(input('which you riddle number (between 1 and 10): '))

        except Exception as ex:
            print('Only supported number, try again')
            continue

        # if nuser input the same number of riddle number, end game and congrat you
        if get_user == get_number:
            print('You winner!!')
            print(end.center(50, '#'))
            get_user_end_or_continue = input('You want end or continue: ')

            if get_user_end_or_continue == 'end':
                button = False
            else:
                continue

        # if number is mynor of the riddle number, continue game
        elif get_user < get_number:
            print(f"{get_user}. It's less than the number, but you were close, come on")
            print(f"riddle: {get_number}")
            get_number = random.randrange(1, 10, 1)

            # continue or end game
            get_user_end_or_continue = input('You want end or continue: ')
            if get_user_end_or_continue == 'end':
                print(end.center(50, '#'))
                button = False
            else:
                continue

        # if number is elderly of the riddle number, continue game
        elif get_user > get_number:
            print(f"{get_user} It's older, but don't stop trying")
            print(f"riddle: {get_number}")
            get_number = random.randrange(1, 10, 1)
            get_user_end_or_continue = input('You want end or continue: ')

            # if you input end, the game is end, else if user input continue, the game continue
            if get_user_end_or_continue == 'end':
                print(end.center(50, '#'))
                button = False
            else:
                continue







riddleGame()

