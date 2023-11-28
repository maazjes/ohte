```mermaid
classDiagram
    class UI{
        create_grid()
        on_window_resize()
        on_entry_change()
    }
    class Sudoku{
        validate()
    }
    UI --|> Sudoku
```