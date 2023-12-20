# Vaatimusmäärittely

Sovellus generoi satunnaisia sudokuita, joita käyttäjä voi ratkaista. Ratkaisu tarkistetaan, kun kaikkiin ruutuihin on lisätty numero.
Käyttäjä voi myös vaihtaa generoitavien sudokujen vaikeustasoa ja kokoa. Vaikeustasoa voi vaihtaa vaihtamalla tyhjien ruutujen määrää.
Lisäksi kaikki syötteet käyttöliittymään validoidaan. Käyttäjän ei ole esimerkiksi mahdollista lisätä 9x9 Sudokuun lukua 10 eikä merkata tyhjien ruutujen määräksi 90.

## Toiminnallisuudet

- [x] Vaikeustason muuttaminen
- [x] Ratkaisun automaattinen tarkistus
- [x] Ruutuun numeron lisääminen numeronäppäimillä
- [x] Sudokun koon muuttaminen
- [x] Syötteiden validointi
- [x] Uuden sudokun generointi
- [x] Peleistä tilastojen pitäminen

## Jatkokehitysideoita

- [ ] Vaikeustason määrittely monipuolisemmin, kun pelkän tyhjien ruutujen lukumäärän perusteella.
- [ ] Käyttäjän luominen ja sijoitusten ylläpito verrattuna muihin käyttäjiin tulostaululla.
- [ ] Sudokun ratkaisija, joka ratkaisee Sudokun ja visualisoi ratkaisuprosessin.