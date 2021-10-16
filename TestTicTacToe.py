import unittest

import TicTacToe


class MyTestCase(unittest.TestCase):
    def test_check_win(self):
        self.assertEqual(TicTacToe.check_win(['X', 'O', 3, 'X', 'O', 6, 'X', 8, 9]), 'X')
        self.assertEqual(TicTacToe.check_win(['X', 'O', 'O', 4, 'X', 6, 7, 8, 'X']), 'X')


if __name__ == '__main__':
    unittest.main()
