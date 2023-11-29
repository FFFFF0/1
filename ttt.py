from os import system


def grid(cells):
    grid = (f"|{cells[1]}|{cells[2]}|{cells[3]}|\n"
            f"|{cells[4]}|{cells[5]}|{cells[6]}|\n"
            f"|{cells[7]}|{cells[8]}|{cells[9]}|\n")
    print(grid)
def check(turn):
    if turn % 2 == 0: return 'O'
    else: return 'X'
def win_condition(cells):
    if         (cells[1] == cells[2] == cells[3]) \
            or (cells[4] == cells[5] == cells[6]) \
            or (cells[7] == cells[8] == cells[9]):
        return True
    elif       (cells[1] == cells[4] == cells[7]) \
            or (cells[2] == cells[5] == cells[8]) \
            or (cells[3] == cells[6] == cells[9]):
        return True
    elif       (cells[1] == cells[5] == cells[9]) \
            or (cells[3] == cells[5] == cells[7]):
        return True
    else:
        return False
cells = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
start = True
finish = False
turn = 0
prev_turn = -1


while start:
    system('cls')
    grid(cells)
    if prev_turn == turn:
        print("Cell is already taken, pick another one.")
    prev_turn == turn
    print("Player" + str((turn % 2) +1) + " turn: Pick a cell to fill. Type end to quit.")
    choice = input()
    if choice == 'end':
        start = False
    elif str.isdigit(choice) and int(choice) in cells:
        if not cells[int(choice)] in {"X", "O"}:
            turn += 1
            cells[int(choice)] = check(turn)

    if win_condition(cells): start, finish = False, True
    if turn > 8: start = False

system('cls')
grid(cells)
if finish:
    if check(turn) == 'X': print("Player 1 wins")
    else: print("Player 2 wins")
else:
    print("Tie")
