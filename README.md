# Sudoku

Ohjelma generoi satunnaisia Sudokuita, joiden kokoa ja vaikeustasoa voi muuttaa. Vaikeustaso muutetaan muuttamalla Sudokussa olevien tyhjien ruutujen lukumäärää. Kun Sudokun ruutuun lisätään virheellinen numero, ruudussa olevan numeron väri muuttuu punaiseksi. Lisäksi voitetuista peleistä lisätään SQLite-tietokantaan dataa, jota voi myöhemmin tarkastella taulukkomuodossa.


## Dokumentaatio

- [Käyttöohje](dokumentaatio/kayttoohje.md)  
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)  
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)  
- [Testausdokumentti](dokumentaatio/testaus.md)  
- [Changelog](dokumentaatio/changelog.md)  
- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)  
- [Release](https://github.com/maazjes/ohte/releases/tag/viikko5)

## Asennus

Asenna riippuvuudet komennolla:

```bash
poetry install
```

Käynnistä Ohjelma komennolla:

```bash
poetry run invoke start
```

Jos käytät Visual Studio Codea, niin kannattaa asentaa lisäosa "Mypy Type Checker". Mypylle on määritelty projektissa valmiiksi konfiguraatiotiedosto.
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