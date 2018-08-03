# Tietokantasovellus-kurssin harjoitustyö: Aineistonkuulustelija

Projekti on web-sovellus, joka toimii opiskelijan apuvälineenä kokeisiin valmistautumisessa. "Tenttibotti" kuulustelee käyttäjää hänen tietokantaan syöttämänsä aineiston (kysymysten, joille mallivastaukset) perusteella.

Sovellus voi auttaa esimerkiksi, kun koealueena on kirja (ei välttämättä valmiilla harjoitustöillä varustettu oppikirja). Opiskelija voi aineiston sisäistämiseksi muodostaa harjoituskysymyksiä ja mallivastauksia omista alleviivauksistaan ja muistiinpanoistaan.

Tenttaus tapahtuu kysymys kerrallaan, satunnaisessa järjestyksessä. Käyttäjän syötettyä oma vastauksensa, näytetään mallivastaus. Tämän jälkeen käyttäjä voi arioida osaamistaan vertaamalla sitä mallivastaukseen ja asettamalla vastaukselleen arvosanan. Kuulusteluaineistoa voi rajata itsearvioinnin perusteella.

Linkki herokuun: https://tenttibot.herokuapp.com/

## Perusversion toiminnallisuus

* Kirjautuminen
* Aineiston (kysymyslistan) lisääminen (ja muutos)
* Kysymysten lisääminen (ja muutos)
* Kysymysten listaaminen
* Mallivastausten lisääminen (ja muutos)
* Mallivastausten listaaminen
* Itsearviointien lisääminen (ja muutos)
* Itsearviointien listaaminen
* Kysymys-mallivastausparien listaaminen, itsearvioinneilla ja ilman
* Kuulustelu-looppi

## Korkean kurssiarvosanan laajuuteen tähtäävät ominaisuudet

* Toimiva tietokantaa käyttävä web-sovellus.
* Käyttäjä, Kysymys +1+ (mallivastaus?) (Vähintään kolme tietokohdetta, eli vähintään 3 tietokantataulua sekä mahdolliset liitostaulut.) 
* Käyttäjällä vähintään 1-moneen-suhde aineiston kanssa (Kirjautumisen lisäksi käyttäjä on yhdistetty tietokannassa johonkin tietokohteeseen)
* Kysymyksiin ja vastauksiin täysi CRUD (Vähintään kahdesta tietokohteesta täysi CRUD (eli luomis-, lukemis-, päivitys-, ja poistotoiminnallisuus)).
* Ehkä useamman käyttäjän välillä jaettu aineisto (Yksi tai useampi monesta moneen -suhde).
* Yhteenvetokyselyjä: Kysymys-mallivastausparit itsearvioinneilla ja ilman, mallivastausten ja käyttökerran vastausten rinnastus, käyttäjäkohtaiset itsearvioinnit päivämäärien mukaan: joka kysymyksen ja koko aineiston arviointien kehityksen seuranta. Hyödynnettäviä tietokantatauluja: Käyttäjä(id, salasana, rekisteröity?), (Aineisto?(id, kysymykset, luotu, muokattu)) Kysymys(kysymys, mallivastaus, vastaus, itsearviointi, luotu, muokattu).
* Laadukkaat käyttötapaukset

## Jatkokehitysideoita

* Aineistojen jakaminen (ilman itsearviointia) käyttäjien välillä
* Pelkkien kysymysten jakaminen käyttäjien välillä
* Mahdollisuus aineistojen tallentamiseen paikallisesti
* Desktop-sovellus
* UI usealle kielelle
