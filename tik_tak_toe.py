def check_win(player, rows):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(rows[i][j] == player for j in range(3)) or all(rows[j][i] == player for j in range(3)):
            return True
    if all(rows[i][i] == player for i in range(3)) or all(rows[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(rows):
    # Check for a draw
    return all(cell != ' ' for row in rows for cell in row)

def print_result(rows):
    if check_win('X', rows):
        print('X wins')
    elif check_win('O', rows):
        print('O wins')
    else:
        print('Draw')

def set_coordinates(player, rows, occupied_cells) -> bool:
    try:
        x, y = map(int, input().split())

        if x not in range(1, 4) or y not in range(1, 4):
            print('Coordinates should be from 1 to 3!')
            return False
        elif (x, y) in occupied_cells:
            print('This cell is occupied! Choose another one!')
            return False
        else:
            rows[x - 1][y - 1] = player
            occupied_cells.add((x, y))  # Mark the cell as occupied
            return True
    except ValueError:
        print('You should enter numbers!')
        return False

def print_board(rows):
    print('---------')
    for row in rows:
        print(f'| {" ".join(row)} |')
    print('---------')

def main():
    symbols = ' ' * 9  # Initialize an empty grid
    rows = [[*symbols[x:x + 3]] for x in range(0, len(symbols), 3)]

    occupied_cells = set()  # Maintain a set of occupied cell coordinates

    current_player = 'X'
    print_board(rows)

    while True:
        valid = False
        while not valid:
            valid = set_coordinates(current_player, rows, occupied_cells)
        print_board(rows)

        if check_win(current_player, rows):
            print_result(rows)
            break
        elif check_draw(rows):
            print_result(rows)
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
