# Tietokantasovellus-kurssin harjoitustyö: Aineistonkuulustelija

Projekti on web-sovellus, joka toimii opiskelijan apuvälineenä kokeisiin valmistautumisessa. "Tenttibotti" kuulustelee käyttäjää hänen tietokantaan syöttämänsä aineiston (kysymysten, joille mallivastaukset) perusteella.

Sovellus voi auttaa esimerkiksi, kun koealueena on kirja (ei välttämättä valmiilla harjoitustöillä varustettu oppikirja). Opiskelija voi aineiston sisäistämiseksi muodostaa harjoituskysymyksiä ja mallivastauksia omista alleviivauksistaan ja muistiinpanoistaan.

Tenttaus tapahtuu kysymys kerrallaan, satunnaisessa järjestyksessä. Käyttäjän syötettyä oma vastauksensa, näytetään mallivastaus. Tämän jälkeen käyttäjä voi arvioida osaamistaan vertaamalla sitä mallivastaukseen. Kuulusteluaineistoa voi rajata itsearvioinnin perusteella.

Aineistoa voi myös jakaa, esimerkiksi lukupiirin kesken. Myös opettaja voi käyttää sovellusta työkaluna: luoda opiskelijoille tai yhdessä opiskelijoiden kanssa kuulustelumateriaalin, antaa opiskelijoille tehtäväksi luoda omat aineistot (mitkä ehkä palautettaisiin) tai jopa korvata kurssikokeen sovellusta hyödyntäen.

## Testitunnukset:

Username: hello
Password: world

## Linkkejä

[Sovellus Herokussa](https://tenttibot.herokuapp.com/)

[Käyttäjätarinoita](https://github.com/magael/tenttibot/blob/master/documentation/user_stories.md)

[Tietokantakaavioluonnos](https://github.com/magael/tenttibot/blob/master/documentation/diagram_sketch.md)

## Perusversion toiminnallisuus

* Kirjautuminen
* Aineiston lisääminen (ja muutos)
* Aineistojen jakaminen (ehkä ilman itsearviointia) käyttäjien välillä
* Kysymysten lisääminen (ja muutos)
* Kysymysten listaaminen
* Mallivastausten lisääminen (ja muutos)
* Mallivastausten listaaminen
* Itsearviointien lisääminen (ja muutos)
* Itsearviointien listaaminen
* Kuulustelu-looppi (tms. järjestely, miten kuulustelu tapahtuu yllä kuvatulla tavalla)

## Korkean kurssiarvosanan laajuuteen tähtäävät ominaisuudet

* Toimiva tietokantaa käyttävä web-sovellus.
* Käyttäjä, Kysymys +1(aineisto?)+ (Vähintään kolme tietokohdetta, eli vähintään 3 tietokantataulua sekä mahdolliset liitostaulut.) 
* Käyttäjällä vähintään yhdestä moneen -suhde aineiston kanssa (Kirjautumisen lisäksi käyttäjä on yhdistetty tietokannassa johonkin tietokohteeseen)
* Kysymyksiin +1 (aineistoon?) täysi CRUD (Vähintään kahdesta tietokohteesta täysi CRUD (eli luomis-, lukemis-, päivitys-, ja poistotoiminnallisuus)).
* Ehkä useamman käyttäjän välillä jaettu aineisto (Yksi tai useampi monesta moneen -suhde).
* Yhteenvetokyselyjä: Kysymys-mallivastausparit itsearvioinneilla ja ilman, mallivastausten ja käyttökerran vastausten rinnastus, käyttäjäkohtaiset itsearvioinnit päivämäärien mukaan.
* Laadukkaat käyttötapaukset

## Jatkokehitysideoita

* Pelkkien kysymysten jakaminen käyttäjien välillä
* Julkisten aineistojen kommentointi
* Mahdollisuus aineistojen tallentamiseen paikallisesti (ehkä myös tulostukseen sopivassa muodossa) (+ ehkä muokkaus ja lataus takaisin)
* Desktop-sovellus
* UI usealle kielelle
