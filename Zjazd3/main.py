import random


def generate_board(A, B):
    board = [[' ' for _ in range(B)] for _ in range(A)]

    start = (random.randint(0, A - 1), random.choice([0, B - 1]))
    stop = (random.randint(0, A - 1), random.choice([0, B - 1]))
    while abs(start[0] - stop[0]) + abs(start[1] - stop[1]) <= 1:
        stop = (random.randint(0, A - 1), random.choice([0, B - 1]))

    board[start[0]][start[1]] = 'A'  # START
    board[stop[0]][stop[1]] = 'B'  # STOP

    obstacles = random.randint(1, (A * B) // 4)
    for _ in range(obstacles):
        x, y = random.randint(0, A - 1), random.randint(0, B - 1)
        if board[x][y] == ' ':
            board[x][y] = 'X'

    return board, start, stop


def display_board(board):
    for row in board:
        print(' '.join(row))
    print()


def move_up(position, board):
    x, y = position
    if x > 0 and board[x - 1][y] != 'X':
        return x - 1, y
    return position


def move_down(position, board):
    x, y = position
    if x < len(board) - 1 and board[x + 1][y] != 'X':
        return x + 1, y
    return position


def move_left(position, board):
    x, y = position
    if y > 0 and board[x][y - 1] != 'X':
        return x, y - 1
    return position


def move_right(position, board):
    x, y = position
    if y < len(board[0]) - 1 and board[x][y + 1] != 'X':
        return x, y + 1
    return position


def display_board_with_position(board, position):
    board_with_player = [row[:] for row in board]
    x, y = position
    board_with_player[x][y] = 'P'
    display_board(board_with_player)


def play_game(board, start, stop):
    position = start
    print("Początkowa pozycja:", position)

    while position != stop:
        display_board_with_position(board, position)
        move = input("Podaj ruch (up, down, left, right): ").strip().lower()
        if move == 'up':
            new_position = move_up(position, board)
        elif move == 'down':
            new_position = move_down(position, board)
        elif move == 'left':
            new_position = move_left(position, board)
        elif move == 'right':
            new_position = move_right(position, board)
        else:
            print("Nieprawidłowy ruch! Spróbuj ponownie.")
            continue

        if new_position == position:
            print("Nie można wykonać ruchu. Spróbuj ponownie.")
        else:
            position = new_position

    print("Gratulacje! Dotarłeś do celu!")


if __name__ == "__main__":
    A, B = 5, 5
    board, start, stop = generate_board(A, B)

    print("Wygenerowana plansza:")
    display_board(board)
    print("START:", start, "STOP:", stop)

    print("\nRozpoczynamy grę!")
    play_game(board, start, stop)
