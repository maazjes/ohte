# Sudoku

Ohjelma generoi satunnaisia Sudokuita, joiden kokoa ja tyhjien ruutujen lukumäärää voi muuttaa. Kun Sudokun ruutuun lisätään virheellinen numero, numeron väri muuttuu punaiseksi. Sudokun ollessa täynnä käyttäjälle avautuu uusi ikkuna, jos ratkaisu on oikein. Lisäksi voitetuista peleistä lisätään SQLite-tietokantaan dataa, jota voi myöhemmin tarkastella taulukkomuodossa.


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

Jos käytät Visual Studio Codea ja haluat kehittää projektia pidemmälle, niin kannattaa asentaa lisäosa "Mypy Type Checker". VSCoden asetuksille ja Mypylle on määritelty projektissa valmiiksi konfiguraatiotiedostot.
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