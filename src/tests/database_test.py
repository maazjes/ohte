import unittest
from database import Database


class TestDatabase(unittest.TestCase):
    def setUp(self) -> None:
        self.database = Database("testing.db")

    def test_insert_game(self) -> None:
        moves = 10
        empty_cells = 5

        self.database.insert_game(5525, moves, empty_cells)
        self.database.cur.execute("SELECT * FROM games ORDER BY id DESC LIMIT 1")
        last_row = self.database.cur.fetchone()

        self.assertIsNotNone(last_row, "No record inserted")
        self.assertEqual(last_row[2], moves, "Moves value mismatch")
        self.assertEqual(last_row[3], empty_cells, "Empty cells value mismatch")

    def test_get_games(self) -> None:
        self.database.insert_game(20, 20, 10)
        records = self.database.get_games()
        self.assertTrue(len(records) > 0, "No records retrieved")
