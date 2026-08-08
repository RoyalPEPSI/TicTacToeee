import random as r
import time

table = ['', '', '', '', '', '', '', '', '']

while True:
    start = input("Do you want to be X or O? ")
    if start == 'X':
        player = 'X'
        ai = 'O'
        break
    elif start == 'O':
        player = 'O'
        ai = 'X'
        break
    else:
        print("Invalid, must be X/O.")


def print_board():
    print(f"{table[0]} | {table[1]} | {table[2]}")
    print("---------")
    print(f"{table[3]} | {table[4]} | {table[5]}")
    print("---------")
    print(f"{table[6]} | {table[7]} | {table[8]}")
print("0 | 1 | 2")
print("---------")
print("3 | 4 | 5")
print("---------")
print("6 | 7 | 8")

remain = [0, 1, 2, 3, 4, 5, 6, 7, 8]
wl = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
      [0, 3, 6], [1, 4, 7], [2, 5, 8],
      [0, 4, 8], [2, 4, 6]]

player_scores = []
ai_scores = []
win = False
lose = False

def check_win():
    for line in wl:
        if all(square in player_scores for square in line):
            return line
    return None

def check_lose():
    for line in wl:
        if all(square in ai_scores for square in line):
            return line
    return None

def player_move():
    try:
        n = int(input("Your move: "))
    except ValueError:
        print("Invalid, must be integer.")
        player_move()
        return

    if n not in range(9):
        print("Invalid, must be in range(0 - 8)")
        player_move()
        return

    if n not in remain:
        print(f"Invalid, position {n} is already claimed.")
        return
    
    table[n] = player
    player_scores.append(n)
    remain.remove(n)
    print_board()

def ai_move():
    time.sleep(1)
    n = r.choice(remain)
    print(f"AI's move: {n}")
    table[n] = ai
    ai_scores.append(n)
    remain.remove(n)
    print_board()



def game():
    try:
        if player == 'X':
            player_move() # player move 1
            ai_move() # ai move 1
            player_move() # player move 2
            ai_move() # ai move 2
            player_move() # player move 3
            win = check_win()
            if win:
                print("You win!")
            else:
                ai_move() # ai move 3
                lose = check_lose()
                if lose:
                    print("AI wins!")
                else:
                    player_move() # player move 4
                    win = check_win()
                    if win:
                        print("You win!")
                    else:
                        ai_move() # ai move 4
                        lose = check_lose()
                        if lose:
                            print("AI wins!")
                        else:
                            player_move() # player move 5
                            win = check_win()
                            if win:
                                print("You win!")
                            else:
                                print("Tie!")



        else:
            ai_move() # ai move 1
            player_move() # player move 1
            ai_move() # ai move 2
            player_move() # player move 2
            ai_move() # ai move 3
            lose = check_lose()
            if lose:
                print("AI wins!")
            else:
                player_move() # player move 3
                win = check_win()
                if win:
                    print("You win!")
                else:
                    ai_move() # ai move 4
                    lose = check_lose()
                    if lose:
                        print("AI wins!")
                    else:
                        player_move() # player move 4
                        win = check_win()
                        if win:
                            print("You win!")
                        else:
                            ai_move() # ai move 5
                            lose = check_lose()
                            if lose:
                                print("AI wins!")
                            else:
                                print("Tie!")





    except IndexError:
        print("Out of range, must be 0 - 8")
        game()
    except ValueError:
        print("Invalid, must be integer.")
        game()

game()