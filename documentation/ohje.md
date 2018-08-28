# Käyttöohje ja asennus

Sovellusta voidaan käyttää joko testipalvelimella tai paikallisesti virtuaaliympäristössä.

[Sovellus Herokussa](https://tenttibot.herokuapp.com/)

## Käyttöohje

Kirjautumattomana käyttäjänä voit tarkastella etusivulla tai ylävalikon linkeistä navigoimalla aiemmin luotuja aihealueita, sekä niiden sisältämiä kysymyksiä. Etusivulla näet myös otsikon oikealla puolella luvun, kuinka monta kysymystä kukin aineisto sisältää. Kysymysten listauksessa näet myös aiheen luojan nimimerkin.

Mikäli sinulla on käyttäjätunnus, voit kirjautua sisään etusivun ylälaidan tai yläpalkin oikean laidan linkistä, mistä sinut ohjataan kirjautumislomakkeeseen.

Voit rekisteröityä yläpalkin oikean laidan tai kirjautumislomakkeen linkistä, mistä pääset rekisteröitymislomakkeeseen. Sovellus kertoo sinulle, jos yrität esimerkiksi käyttää jo varattua käyttäjätunnusta, tai liian lyhyttä salasanaa.

Kirjauduttuasi sisään voit luoda uusia aihealueita etusivun ylälaitaan ilmestyneestä painikkeesta.

Aihealueen sisällä voit luoda uusia kysymyksiä ylälaidan painikkeesta. Näet kysymysten tekstin oikealla puolella luvun, joka kertoo, kuinka hyvin koet tällä hetkellä hallitsevasi kysymyksen vastauksen. Kunkin kysymyksen oikealla puolella sijaitsevasta painikkeesta pääset lomakkeeseen, jossa voit lisätä kysymykselle mallivastauksen ja päivittää sitä, muokata kysymysten tekstiä ja itsearviointia sekä poistaa kysymyksiä.

Järjestelmänvalvojana kirjautuneena voit käyttää etusivulla sijaitsevaa linkkiä, josta pääset listaamaan kaikki käyttäjätunnukset ja niihin liittyvät käyttäjäroolit.

## Sovelluksen käyttö paikallisesti

## Vaatimukset:

Tarvitset tuen Python-kielisten ohjelmien suorittamiseen: vähintään Pythonin version 3.5 (https://www.python.org/downloads/).

Samalla sinun tulee ladattua kirjastojen lataamiseen tarvittava pip, sekä "virtuaaliympäristöjen" luomiseen tarvittava venv-kirjasto.


### Asennus ja käynnistys:

1. Kloonaa tai lataa ja pura projekti [repositorion etusivulta](https://github.com/magael/tenttibot).

2. Navigoi projektin juureen komentokehotteella ja asenna virtuaaliympäristö komennolla

```
python3 -m venv venv
```

3. Aktivoi virtuaaliympäristö:

```
source venv/bin/activate
```

4. Lataa projektin riippuvuudet:

```
"pip install -r requirements.txt"
```

5. Käynnistä sovellus:

```
python run.py
```

6. Sovellusta voi nyt käyttää osoitteessa http://localhost:5000/ tai http://127.0.0.1:5000/.

### Admin-roolin lisääminen:

1. Rekisteröidy sovelluksessa, esimerkiksi nimimerkillä admin.

2. Avaa SQLite komentokehotteesa, sovelluksen juuressa komennolla

```
sqlite3 application/questions.db
```

3. Alustetaan rooleihin järjestelmänvalvoja:
```
INSERT INTO Role (name) VALUES ('ADMIN');
```

4. Lisätäksesi admin-roolin "admin"-nimiselle käyttäjälle syötä seuraava SQL-komento:

```
UPDATE user_roles SET role_id = (SELECT id FROM Role r WHERE r.name = 'ADMIN')
 WHERE account_id IN (SELECT id FROM account WHERE account.username = 'admin');
```

5. Nyt admin-rooli on lisätty valitsemallesi käyttäjälle. Voit varmistaa asian esimerkiksi listaamalla kaikkien käyttäjien roolit kyselyllä

```
SELECT a.username, r.name FROM account a
 LEFT JOIN Role r ON a.id IN (SELECT account_id FROM user_roles ur WHERE ur.account_id = a.id AND ur.role_id = r.id)
  GROUP BY r.name, a.username;
```

  tai admin-tunnuksilla kirjautuneena linkistä "Users".

  Voit lisätä kohdan 3 jälkeen myös lisää järjestelmänvalvojia toistamalla kohdat 1 ja 4 haluamallasi toisella käyttäjätunnuksella, esim.

```
"...WHERE account.username = 'adminkakkonen');"
```