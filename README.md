# Sudoku

Sovellus generoi satunnaisia sudokuita, joita käyttäjä voi ratkaista. Ratkaisu tarkistetaan, kun kaikkiin ruutuihin on lisätty numero.
Generoitavien sudokujen vaikeustasoa voi muuttaa muuttamalla tyhjien ruutujen määrää.


## Dokumentaatio

[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)  
[Changelog](dokumentaatio/changelog.md)  
[Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)  
[Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)  
[Käyttöohje](dokumentaatio/kayttoohje.md)  
[Release](https://github.com/maazjes/ohte/releases/tag/viikko5)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```