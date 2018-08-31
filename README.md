# Tietokantasovellus-kurssin harjoitustyö: Aineistonkuulustelija

Projekti on web-sovellus, joka toimii oppimisen apuvälineenä. "Tenttibotti" kuulustelee käyttäjää hänen tietokantaan syöttämänsä aineiston perusteella.

Sovellus voi auttaa esimerkiksi pääsykokeisiin lukemisessa, mutta myös muut kuin opiskelijat voivat hyötyä sovelluksen käyttämisestä. Käyttäjä, jolla on tavoitteena esimerkiksi opetella kirjan sisältö, voi muodostaa harjoituskysymyksiä ja mallivastauksia omista alleviivauksistaan ja muistiinpanoistaan.

Tenttaus tapahtuu tarkastelemalla vapaasti valitun aineiston kysymyskortteja yksi kerrallaan. Käyttäjän annettua oma vastauksensa näytetään mallivastaus. Tämän jälkeen käyttäjä voi arvioida osaamistaan vertaamalla viimeisintä vastaustaan mallivastaukseen. Itsearvioinnit auttavat rajaamaan kuulusteluaineistoa.

Paras tapa oppia on luoda kuulusteluaineisto itse itselleen, mutta sovellus voi myös toimia esimerkiksi lukupiirin kanssa yhteisesti käytettynä. Lisäksi käyttäjä voi löytää muiden tekemiä aineistoja aiheista, joita ei edes tiennyt haluavansa opetella. Myös opettajat voivat käyttää sovellusta eräänä opetusmenetelmänä.

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

[Jatkokehitysideoita](https://github.com/magael/tenttibot/blob/master/documentation/jatkokehitys.md)

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
    PRIMARY KEY (id)
    FOREIGN KEY(subject_id) REFERENCES subject (id)
);

CREATE TABLE mastery (
    id INTEGER NOT NULL,
    mastery INTEGER NOT NULL
    FOREIGN KEY(account_id) REFERENCES account (id)
    FOREIGN KEY(question_id) REFERENCES question (id)
    PRIMARY KEY (id)
);
```

## Perusversion toiminnallisuuksia

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