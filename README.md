# Tietokantasovellus-kurssin harjoitustyö: Aineiston kuulustelija

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

## Jatkokehitysideoita

* Aineistojen jakaminen (ilman itsearviointia) käyttäjien välillä
* Pelkkien kysymysten jakaminen käyttäjien välillä
* Mahdollisuus aineistojen tallentamiseen paikallisesti
* Desktop-sovellus
* UI usealle kielelle
