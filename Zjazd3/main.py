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

    return board, start, stop,


def display_board(board):
    for row in board:
        print(' '.join(row))
    print()


def move(position, direction, board):
    x, y = position
    if direction == 'up' and x > 0 and board[x - 1][y] != 'X':
        return x - 1, y
    elif direction == 'down' and x < len(board) - 1 and board[x + 1][y] != 'X':
        return x + 1, y
    elif direction == 'left' and y > 0 and board[x][y - 1] != 'X':
        return x, y - 1
    elif direction == 'right' and y < len(board[0]) - 1 and board[x][y + 1] != 'X':
        return x, y + 1
    return position


def display_board_with_position(board, position):
    board_with_player = [row[:] for row in board]
    x, y = position
    board_with_player[x][y] = 'P'
    display_board(board_with_player)


def is_path_possible(start, stop, board):
    visited = set()

    def dfs(x, y):
        if (x, y) == stop:
            return True
        if (x, y) in visited or x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] == 'X':
            return False
        visited.add((x, y))
        return any(dfs(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)])

    return dfs(start[0], start[1])


def play_game(board, start, stop):
    position = start
    print("Początkowa pozycja:", position)

    while position != stop:
        display_board_with_position(board, position)
        move_direction = input("Podaj ruch (up, down, left, right): ").strip().lower()
        position = move(position, move_direction, board)

        if position == start:
            print("Nie można wykonać ruchu. Spróbuj ponownie.")
        else:
            start = position

    print("Gratulacje! Dotarłeś do celu!")


if __name__ == "__main__":
    A, B = 5, 5
    board, start, stop = generate_board(A, B)

    print("Wygenerowana plansza:")
    display_board(board)
    print("START:", start, "STOP:", stop)

    print("\nRozpoczynamy grę!")
    play_game(board, start, stop)
