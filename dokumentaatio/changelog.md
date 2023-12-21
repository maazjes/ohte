## Viikko 3

- Lisätty Sudoku-luokka, joka luo satunnaisen sudokun ja tarkistaa tarvittaessa itsensä

## Viikko 4

- Lisätty alkukantainen UI, joka on yhdistetty sovelluslogiikkaan
- Sudokun ollessa täynnä, UI tarkistaa sudokun ja printtaa konsoliin, onko se oikein vai väärin

## Viikko 5

- Lisätty asetukset-paneeli, josta voi vaihtaa tyhjien ruutujen määrää sudokussa. Base-asetus ei vielä toimi

## Viikko 6

- Base-valinta toimii
- Käyttäjä ei voi enää lisätä vääriä lukuja ruutuihin
- Pienemmät ruudukot erotettu isommasta ruudukosta
- Painike uuden satunnaisen Sudokun generoimiseksi
- Kun käyttäjä on ratkaissut Sudokun, hän saa palautetta sen oikeellisuudesta uudessa ikkunassa

## Viikko 7

- Pelatuista peleistä tallennetaan pelitietoja SQLite-tietokantaan
- Tallennettuja pelitietoja voi tarkastella taulukkomuodossa "Stats"-ikkunasta, jonka saa auki valikosta
    - Taulukon rivit voi järjestää sarakkeen mukaan painamalla sarakkeen otsikkoa
- Sudokun ruudussa olevan numeron väri muuttuu punaiseksi, jos se on väärin