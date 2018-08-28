# Tietokantasovellus-kurssin harjoitustyö: Aineistonkuulustelija

Projekti on web-sovellus, joka toimii opiskelijan apuvälineenä kokeisiin valmistautumisessa. "Tenttibotti" kuulustelee käyttäjää hänen tietokantaan syöttämänsä aineiston perusteella.

Sovellus voi auttaa esimerkiksi, kun koealueena on kirja (ei välttämättä valmiilla harjoitustöillä varustettu oppikirja). Opiskelija voi materiaalin sisäistämiseksi muodostaa harjoituskysymyksiä ja mallivastauksia omista alleviivauksistaan ja muistiinpanoistaan.

Tenttaus tapahtuu kysymys kerrallaan, satunnaisessa järjestyksessä. Käyttäjän annettua oma vastauksensa näytetään mallivastaus. Tämän jälkeen käyttäjä voi arvioida osaamistaan vertaamalla viimeisintä vastaustaan mallivastaukseen. Kuulusteluaineistoa voi rajata itsearvioinnin perusteella.

Aineistoa voi myös jakaa, esimerkiksi lukupiirin kesken. Myös opettaja voi käyttää sovellusta työkaluna: luoda opiskelijoille tai yhdessä opiskelijoiden kanssa kuulustelumateriaalin, antaa opiskelijoille tehtäväksi luoda omat aineistot (mitkä ehkä palautettaisiin), ehkä jopa korvata kurssikokeen sovellusta hyödyntäen.

## Testitunnukset

Tavallinen käyttäjä:<br>
Username: hw<br>
Password: hello123

Admin:<br>
Username: admin<br>
Password: admin123

## Linkkejä

[Sovellus Herokussa](https://tenttibot.herokuapp.com/)

[Käyttöohje ja asennus](https://github.com/magael/tenttibot/blob/master/documentation/ohje.md)

[Käyttäjätarinoita](https://github.com/magael/tenttibot/blob/master/documentation/user_stories.md)

[Tietokantakaavio](https://github.com/magael/tenttibot/blob/master/documentation/diagram.png)

## CREATE TABLE -lauseet

```
CREATE TABLE account (
    id INTEGER NOT NULL,
    date_created DATETIME, 
	date_modified DATETIME,
    name VARCHAR(144) NOT NULL,
    username VARCHAR(144) NOT NULL,
    password VARCHAR(144) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE user_roles (
    account_id INTEGER NOT NULL
    role_id INTEGER NOT NULL
    FOREIGN KEY(account_id) REFERENCES account (id)
    FOREIGN KEY(role_id) REFERENCES role (id)
);

CREATE TABLE role (
    id INTEGER NOT NULL,
    date_created DATETIME, 
	date_modified DATETIME,
    name VARCHAR(144) NOT NULL
    PRIMARY KEY (id)
);

CREATE TABLE user_subjects (
    account_id INTEGER NOT NULL
    subject_id INTEGER NOT NULL
    FOREIGN KEY(account_id) REFERENCES account (id)
    FOREIGN KEY(subject_id) REFERENCES subject (id)
);

CREATE TABLE subject (
    id INTEGER NOT NULL,
    date_created DATETIME, 
	date_modified DATETIME,
    name VARCHAR(144) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE question (
    id INTEGER NOT NULL,
    date_created DATETIME, 
	date_modified DATETIME,
    name VARCHAR(144) NOT NULL,
    answer VARCHAR(144) NOT NULL,
    mastery INTEGER NOT NULL
    PRIMARY KEY (id)
    FOREIGN KEY(subject_id) REFERENCES subject (id)
);
```

## Perusversion toiminnallisuus

* Rekisteröityminen ja kirjautuminen
* Aihealueiden lisääminen, muutos ja poisto
* Aihealueiden listaaminen
* Kysymysten lisääminen, muutos ja poisto
* Kysymysten listaaminen
* Mallivastausten lisääminen (ja muutos, poisto)
* Mallivastausten listaaminen
* Itsearviointien lisääminen (ja muutos, poisto)
* Itsearviointien listaaminen
* Käyttäjien ja roolien listaaminen (admin)
* Kuulusteluaineisto ja -näkymä

## Ominaisuuksien erittelyä

* Toimiva tietokantaa käyttävä web-sovellus.
* Tietokohteet: Käyttäjä, Aihealue, Kysymys (väh. 3 tietokantataulua sekä mahdolliset liitostaulut).
* Kirjautumisen lisäksi käyttäjä on yhdistetty tietokannassa aineistoon (Aihealueeseen).
* Kysymyksiin ja Aihealueisiin täysi CRUD.
* Monesta moneen -suhteita: Käyttäjien aiheet ja roolit. Ehkä "KuulusteluKysymykset" tms.
* Yhteenvetokyselyjä: Listataan aihealueet ja niihin liittyvien kysymysten lukumäärä, listataan käyttäjät ja heidän roolinsa, etsitään aihealueen luoja.
* Käyttötapaukset

## Jatkokehitysideoita

* Aineistojen (Aihealueiden) muokkausoikeuksien ja/tai mallivastausten / kuulustelutoiminnallisuuden jakaminen käyttäjien välillä
* Aihealueisiin liittyvät avainsanat, "tagit" ja selailu niiden perusteella
* Hakutoiminnallisuuksia
* Subjects -> Decks, Questions -> Cards
* Kuvien lisäys "kortteihin"
* Muistiinpanot (aihe- ja/tai kysymyskohtaiset)
* Julkisten aineistojen kommentointi
* Algoritmi, joka päättää, milloin minkäkin arvosanan saanut kysymys kysytään uudestaan (vaihtoehtona käyttäjän itse rajaamaan aineistoon)
* Mahdollisuus aineistojen tallentamiseen paikallisesti (ehkä myös tulostukseen sopivassa muodossa) (+ ehkä muokkaus ja lataus takaisin)
* Työpöytäsovellus
* Käyttöliittymä usealle kielelle
* Käyttäjätunnuksen vahvistaminen sähköpostilla ym. "turvallisuuden" kehittämistä
