```mermaid
classDiagram
    class UI{
        create_controls()
        create_grid()
        on_window_resize()
        on_entry_change()
        on_empty_cells_change()
        validate_entry()
    }
    class Sudoku{
        validate()
        generate_sudoku()
        set_base()
        set_empty_cells()
    }
    UI --|> Sudoku
```

```mermaid
sequenceDiagram
    participant K as Käyttäjä
    participant UI as UI
    participant G as Sudoku

    K->>UI: Syöttää numeron ruutuun
    UI->>G: Päivittää numeron pelilogiikkaan
    G->>G: Tarkistaa pelitilanteen
    G-->>UI: Ilmoittaa muutoksesta / tilasta
    UI->>UI: Päivittää ruudun näytöllä
```