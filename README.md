# Tietokantasovellus-kurssin harjoitustyö: Aineistonkuulustelija

Projekti on web-sovellus, joka toimii opiskelijan apuvälineenä kokeisiin valmistautumisessa. "Tenttibotti" kuulustelee käyttäjää hänen tietokantaan syöttämänsä aineiston perusteella.

Sovellus voi auttaa esimerkiksi, kun koealueena on kirja (ei välttämättä valmiilla harjoitustöillä varustettu oppikirja). Opiskelija voi materiaalin sisäistämiseksi muodostaa harjoituskysymyksiä ja mallivastauksia omista alleviivauksistaan ja muistiinpanoistaan.

Tenttaus tapahtuu kysymys kerrallaan, satunnaisessa järjestyksessä. Käyttäjän syötettyä oma vastauksensa näytetään mallivastaus. Tämän jälkeen käyttäjä voi arvioida osaamistaan vertaamalla viimeisintä vastaustaan mallivastaukseen. Kuulusteluaineistoa voi rajata itsearvioinnin perusteella.

Aineistoa voi myös jakaa, esimerkiksi lukupiirin kesken. Myös opettaja voi käyttää sovellusta työkaluna: luoda opiskelijoille tai yhdessä opiskelijoiden kanssa kuulustelumateriaalin, antaa opiskelijoille tehtäväksi luoda omat aineistot (mitkä ehkä palautettaisiin), ehkä jopa korvata kurssikokeen sovellusta hyödyntäen.

## Testitunnukset:

Username: hello</br>
Password: world

## Linkkejä

[Sovellus Herokussa](https://tenttibot.herokuapp.com/)

[Käyttäjätarinoita](https://github.com/magael/tenttibot/blob/master/documentation/user_stories.md)

[Tietokantakaavioluonnos](https://github.com/magael/tenttibot/blob/master/documentation/diagram_sketch.md)

## Perusversion toiminnallisuus

* Kirjautuminen
* Aihealueiden lisääminen (ja muutos, poisto)
* Aineistojen (Aihealueiden) jakaminen (ehkä ilman itsearviointia ja/tai (malli)vastauksia) käyttäjien välillä
  * Tai aihealueiden "tägäys", selailu tagien perusteella
* Aihealueiden listaaminen
* Kysymysten lisääminen (ja muutos, poisto)
* Kysymysten listaaminen
* Mallivastausten lisääminen (ja muutos, poisto)
* Mallivastausten listaaminen
* Itsearviointien lisääminen (ja muutos, poisto)
* Itsearviointien listaaminen
* Kuulustelu-looppi (tms. järjestely, miten kuulustelu tapahtuu yllä kuvatulla tavalla)

## Korkean kurssiarvosanan laajuuteen tähtäävät ominaisuudet

* Toimiva tietokantaa käyttävä web-sovellus.
* Tietokohteet: Käyttäjä, Aihealue, Kysymys (väh. 3 tietokantataulua sekä mahdolliset liitostaulut).
* Kirjautumisen lisäksi käyttäjä on yhdistetty tietokannassa aineistoon (Aihealueeseen).
* Kysymyksiin ja Aihealueisiin täysi CRUD.
* Useamman käyttäjän välillä jaettu aineisto (Aihealue) tai aiheiden "tägäys" (yksi tai useampi monesta moneen -suhde).
* Yhteenvetokyselyjä: Tiettyyn aihealueeseen liittyvien kysymysten ja niihin liittyvien arviointien sekä mahdollisesti mallivastausten (ja ehkä viimeisimmän vastauksen) listaus (yksitellen ja kaikki). Tiettyyn käyttäjään liittyvien aihealueiden listaus. Ehkä aihealueiden listaus tagin perusteella. Aihealueen käyttäjäkohtaiset itsearvioinnit päivämäärien mukaan.
* Laadukkaat käyttötapaukset

## Jatkokehitysideoita

* Aihealueisiin liittyvät avainsanat, "tagit"
* Subjects -> Decks, Questions -> Cards
* Kuvien lisäys "kortteihin"
* Pelkkien kysymysten jakaminen käyttäjien välillä
* Muistiinpanot (aihe- ja/tai kysymyskohtaiset)
* Julkisten aineistojen kommentointi
* Algoritmi, joka päättää, milloin minkäkin arvosanan saanut kysymys kysytään uudestaan (vaihtoehtona käyttäjän itse rajaamaan aineistoon)
* Mahdollisuus aineistojen tallentamiseen paikallisesti (ehkä myös tulostukseen sopivassa muodossa) (+ ehkä muokkaus ja lataus takaisin)
* Desktop-sovellus
* Käyttöliittymä usealle kielelle
