import sqlite3


class Database:
    """
    Class that interacts with the database.
    """

    def __init__(self) -> None:
        """
        Initializes a Database object, establishes a connection to the SQLite database,
        and creates a table for storing Sudoku game records if it doesn't exist.

        The table 'games' is structured with columns for ID, time, moves, and empty cells.
        """
        self.con = sqlite3.connect("data.db")
        self.cur = self.con.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            time INTEGER, moves INTEGER, empty INTEGER)"""
        )

    def insert_game(self, seconds: int, moves: int, empty_cells: int) -> None:
        """
        Inserts a Sudoku game record into the database.

        Args:
            seconds (int): Time of the game in seconds.
            moves (int): Number of moves made in the game.
            empty_cells (int): Number of empty cells in the game.

        The method calculates the elapsed time from the start to the current time and
        formats it before storing it along with the number of moves and empty cells in the database.
        """

        def format_time(num: int) -> str:
            formatted_time = ""

            if num == 0:
                formatted_time += "00"
            elif num < 10:
                formatted_time += f"0{num}"
            else:
                formatted_time += f"{num}"

            return formatted_time

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        formatted_time = ""

        formatted_time += f"{format_time(hours)}:"
        formatted_time += f"{format_time(minutes)}:"
        formatted_time += f"{format_time(seconds)}"

        self.cur.execute(
            "INSERT INTO games (time, moves, empty) VALUES (?, ?, ?)",
            (formatted_time, moves, empty_cells),
        )
        self.con.commit()

    def get_games(self) -> list[tuple[int, int, int, int]]:
        """
        Retrieves all game records from the database.

        Returns:
            list[tuple[int, int, int, int]]: List of tuples, each representing a game record.
            Each tuple contains the game ID, formatted time,
            number of moves, and number of empty cells.
        """
        self.cur.execute("select * from games")
        rows: list[tuple[int, int, int, int]] = self.cur.fetchall()
        return rows
