# Vaatimusmäärittely

Ohjelma generoi satunnaisia Sudokuita, joita käyttäjä voi ratkaista. Ratkaisu tarkistetaan, kun kaikkiin ruutuihin on lisätty numero. Käyttäjä voi myös vaihtaa generoitavien Sudokujen kokoa ja tyhjien ruutujen lukumäärää. Kaikki syötteet käyttöliittymään validoidaan. Käyttäjän ei ole esimerkiksi mahdollista lisätä 9x9 Sudokuun lukua 10 eikä merkata tyhjien ruutujen määräksi 90. Pelatut pelit tallennetaan SQLite-tietokantaan, mikä mahdollistaa pelitietojen myöhemmän tarkastelun.

## Toiminnallisuudet

- [x] Tyhjien ruutujen lukumäärän muuttaminen
- [x] Ratkaisun automaattinen tarkistus
- [x] Ruutuun numeron lisääminen numeronäppäimillä
- [x] Sudokun koon muuttaminen
- [x] Syötteiden validointi
- [x] Uuden satunnaisen Sudokun generointi
- [x] Pelien keston, tyhjien ruutujen lukumäärän ja siirtojen lukumäärän tallentaminen SQLite-tietokantaan
- [x] Mahdollisuus tarkastella tallennettuja pelitietoja taulukkomuodossa Stats-ikkunasta
    - [x] Taulukon rivit voi järjestää sarakkeen mukaan painamalla sarakkeen otsikkoa
- [x] Ruudussa olevan numeron väri muuttuu punaiseksi, jos se on väärin
- [x] Valmiiksi täytetyt ruudut ovat harmaita ja niissä olevaa numeroa ei voi muuttaa

## Jatkokehitysideoita

- [ ] Vaikeustason määrittely monipuolisemmin, kun pelkän tyhjien ruutujen lukumäärän perusteella
- [ ] Käyttäjän luominen ja sijoitusten ylläpito verrattuna muihin käyttäjiin tulostaululla
- [ ] Sudokun ratkaisija, joka ratkaisee Sudokun ja visualisoi ratkaisuprosessin