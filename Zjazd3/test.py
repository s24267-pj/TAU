import unittest
from main import move_up, move_down, move_left, move_right


class TestGameLogic(unittest.TestCase):

    def setUp(self):
        self.board = [
            [' ', 'X', ' ', ' ', ' '],
            [' ', ' ', 'X', ' ', ' '],
            [' ', ' ', ' ', ' ', 'X'],
            ['X', ' ', ' ', 'X', ' '],
            [' ', ' ', ' ', ' ', ' ']
        ]

    def test_move_up(self):
        self.assertEqual(move_up((3, 2), self.board), (2, 2), "Nieprawidowy ruch w górę: przeszkoda")
        self.assertEqual(move_up((0, 0), self.board), (0, 0), "Nieprawidowy ruch w górę: wyjście poza planszę.")

    def test_move_down(self):
        self.assertEqual(move_down((3, 4), self.board), (4, 4), "Nieprawidowy ruch w dół: przeszkoda")
        self.assertEqual(move_down((4, 4), self.board), (4, 4), "Nieprawidłowy ruch w dół: : wyjście poza planszę.")

    def test_move_left(self):
        self.assertEqual(move_left((2, 2), self.board), (2, 1), "Nieprawidowy ruch w lewo: przeszkoda")
        self.assertEqual(move_left((3, 0), self.board), (3, 0), "Nieprawidłowy ruch w lewo: wyjście poza planszę.")

    def test_move_right(self):
        self.assertEqual(move_right((2, 2), self.board), (2, 3), "Nieprawidowy ruch w prawo: przeszkoda")
        self.assertEqual(move_right((2, 4), self.board), (2, 4), "Nieprawidłowy ruch w prawo: wyjście poza planszę.")

    def test_reach_goal(self):
        board = [
            [' ', ' ', ' ', ' ', 'B'],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']
        ]
        start = (0, 3)
        stop = (0, 4)

        position = move_right(start, board)

        self.assertEqual(position, stop, "Gracz nie dotarł do mety.")


if __name__ == "__main__":
    unittest.main()
