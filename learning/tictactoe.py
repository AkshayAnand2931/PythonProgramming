def display(choice_list):
    print("\t{}\t|\t{}\t|\t{}".format(choice_list[6],choice_list[7],choice_list[8]))
    print("-"*50)
    print("\t{}\t|\t{}\t|\t{}".format(choice_list[3],choice_list[4],choice_list[5]))
    print("-"*50)
    print("\t{}\t|\t{}\t|\t{}".format(choice_list[0],choice_list[1],choice_list[2]))


def symbol():
    while True:
        sym = input("\nPlayer 1: Choose the symbol you want to play as. (X or O): ")
        if sym in ['X','O']:
            break
        else:
            print("Invalid input. Please choose between X or O (Capitalised).")
    return sym


def player_choice():
    while True:
        choice = input('\nChoose the position you want to play. Imagine the board on your keypad and choose. (1 to 9): ')
        if choice.isdigit() and int(choice) in range(1,10):
            break 
        else:
            print('\nPlease choose a valid input format.')
    return int(choice)

def opp(sym):
    if sym == 'X':
        return 'O'
    else:
        return 'X'

def check_game(choice_list):

    if choice_list[6] == choice_list[7] == choice_list[8] and choice_list[6] in ['X','O']:
        return True,choice_list[6]
    elif choice_list[3] == choice_list[4] == choice_list[5] and choice_list[3] in ['X','O']:
        return True,choice_list[3]
    elif choice_list[0] == choice_list[1] == choice_list[2] and choice_list[0] in ['X','O']:
        return True,choice_list[0]
    elif choice_list[0] == choice_list[3] == choice_list[6] and choice_list[0] in ['X','O']:
        return True,choice_list[0]
    elif choice_list[1] == choice_list[4] == choice_list[7] and choice_list[1] in ['X','O']:
        return True,choice_list[1]
    elif choice_list[2] == choice_list[5] == choice_list[8] and choice_list[2] in ['X','O']:
        return True,choice_list[2]
    elif choice_list[0] == choice_list[4] == choice_list[8] and choice_list[0] in ['X','O']:
        return True,choice_list[0]
    elif choice_list[6] == choice_list[4] == choice_list[2] and choice_list[6] in ['X','O']:
        return True,choice_list[6]
    return False,choice_list[0]


def game(choice_list,sym):

    game_over = False
    turn_1 = True
    count = 0

    while (not game_over) and (count < 9):
        choice = player_choice()
        if turn_1:
            choice_list[choice-1] = sym
        else:
            choice_list[choice-1] = opp(sym)
        
        display(choice_list)

        game_over,winner = check_game(choice_list)
        if winner == sym:
            player = 1
        else:
            player = 2
        
        if game_over:
            print(f'\n {sym} has won the game! Congratulations to Player {player}!!')
        
        count+=1
        turn_1 = not turn_1
        
        if count == 9:
            print('\nThe game was a draw. Better luck next time.')


choice_list = ['','','','','','','','','','']
print("\nWelcome to the tic-tac-toe game.\n\n")
display(choice_list)
sym = symbol()

game(choice_list,sym)