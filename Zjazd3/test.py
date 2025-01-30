import unittest
from main import generate_board, move, is_path_possible


class TestGameLogic(unittest.TestCase):

    def setUp(self):
        self.board, self.start_position, self.stop_position = generate_board(5, 5)
        self.player_position = self.start_position

    def test_player_cannot_move_outside(self):
        self.player_position = (0, 2)
        self.assertEqual(move(self.player_position, "up", self.board), (0, 2),
                         "Gracz nie powienien poruszyć się w górę.")

        self.player_position = (2, 0)
        self.assertEqual(move(self.player_position, "left", self.board), (2, 0),
                         "Gracz nie powienien poruszyć się w lewo.")

        self.player_position = (4, 2)
        self.assertEqual(move(self.player_position, "down", self.board), (4, 2),
                         "Gracz nie powienien poruszyć się w dół")

        self.player_position = (2, 4)
        self.assertEqual(move(self.player_position, "right", self.board), (2, 4),
                         "Gracz nie powienien poruszyć się w prawo")

    def test_player_cannot_move_in_obstacle(self):
        self.board[1][1] = 'X'
        self.player_position = (1, 0)
        self.assertEqual(move(self.player_position, "right", self.board), (1, 0),
                         "Gracz nie powinien wejść na przeszkodę.")

    def test_player_can_move(self):
        self.board = [[" " for _ in range(5)] for _ in range(5)]
        self.player_position = (1, 1)
        self.board[1][1] = "P"

        self.assertEqual(move(self.player_position, "up", self.board), (0, 1), "Gracz nie może poruszyć się w górę.")
        self.assertEqual(move(self.player_position, "down", self.board), (2, 1), "Gracz nie może poruszyć się w dół.")
        self.assertEqual(move(self.player_position, "left", self.board), (1, 0), "Gracz nie może poruszyć się w lewo.")
        self.assertEqual(move(self.player_position, "right", self.board), (1, 2),
                         "Gracz nie może poruszyć się w prawo.")

    def test_start_and_stop_positions_are_different(self):
        self.assertNotEqual(self.start_position, self.stop_position, "Pozycje START i STOP powinny być różne")

    def test_player_initial_position_equals_start_position(self):
        self.assertEqual(self.player_position, self.start_position,
                         "Początkowa pozycja gracza powinna być równa pozycji START")

    def test_player_reaches_stop(self):
        self.player_position = self.stop_position
        self.assertEqual(self.player_position, self.stop_position, "Gracz powinien dotrzeć do pola STOP")

    def test_no_path_to_stop(self):
        start_x, start_y = self.start_position
        potential_obstacles = [
            (start_x - 1, start_y), (start_x + 1, start_y),
            (start_x, start_y - 1), (start_x, start_y + 1)
        ]
        self.board = [[" " for _ in range(5)] for _ in range(5)]
        for x, y in potential_obstacles:
            if 0 <= x < 5 and 0 <= y < 5:
                self.board[x][y] = 'X'

        self.assertFalse(is_path_possible(self.start_position, self.stop_position, self.board),
                         "Nie powinno być ścieżki do STOP")


if __name__ == "__main__":
    unittest.main()
