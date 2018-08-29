# Käyttäjätarinat

### Kirjautumaton käyttäjä

* Kirjautumattomana käyttäjänä näen etusivulla alueiden listauksessa kaikki aineistot, jotta voin valita tarkasteltavaksi minua kiinnostavan aihealueen.
* Kirjautumattomana käyttäjänä näen etusivulla alueiden sisältämien kysymysten lukumäärät, jotta tiedän, mitkä aineistoista ovat tyhjiä ja mitkä laajoja.
  * Yllä oleviin kahteen toiminnallisuuteen liittyvä SQL-kysely:
  ```
  SELECT s.id, s.name, COUNT(q.id) FROM Subject s 
  LEFT JOIN Question q ON q.subject_id = s.id 
  GROUP BY s.id ORDER BY s.date_created DESC;
  ```

###

* Kirjautumattomana käyttäjänä näen alueiden sisältämät kysymykset ja mallivastaukset, jotta voin arvioida kyseisen aineiston (ja sovelluksen ylipäätään) hyödyllisyyttä itselleni.
  ```
  Question.query.filter_by(subject_id=subject_id)
  ```
* Kirjautumattomana käyttäjänä näen kysymysten listauksessa (muun muassa otsikoiden lisäksi) aihealueen luojan, jotta voin erottaa samannimiset aineistot toisistaan, aineiston tekijä saa ansaitsemansa tunnustuksen ja voin esimerkiksi saada selville, että aineisto on jo tuntemani henkilön luoma.
  ```
  SELECT a.username FROM account a
  LEFT JOIN user_subjects us
  ON us.subject_id = *halutun aihealueen id*
  WHERE a.id = us.account_id;
  ```

###

* Kirjautumattomana pystyn rekisteröitymään, jotta minulla on käytettävissäni omat käyttäjätunnukset.
* Kirjautumattomana käyttäjänä pystyn kirjautumaan sisään, jotta pääsen käyttämään kirjautumattomilta käyttäjiltä estettyjä toimintoja, mikäli minulla on tiedossani käyttäjätunnus ja salasana.

### Kirjautunut (tavallinen) käyttäjä

* Kirjautuneena käyttäjänä pystyn luomaan uusia aineistoja / aihealueita (Subject), jotta minulla on otsikko, jonka alle jäsennellä kuulustelumateriaalia.
* Kirjautuneena käyttäjänä voin muokata itse luomieni aineistojen otsikoita, jotta minun ei tarvitse nähdä valtavasti vaivaa uuden aineiston luomiseen, mikäli haluan muuttaa ainestoni nimeä.
* Kirjautuneena käyttäjänä voin poistaa itse luomiani aineistoja, jotta voin pitää sovelluksen ja sen sisäiset omat näkymäni siistinä turhasta informaatiosta, ja esimerkiksi päästä eroon materiaalista, mihin en halua kenenkään pääsevän käsiksi.

###

* Kirjautuneena käyttäjänä voin lisätä itse luomiini aineistoihin uusia kysymyksiä / kuulustelukortteja (Question) ja niihin mallivastaukset ja osaamisen lähtötasot, jotta minulla on materiaalia, mitä kuulustella.
* Kirjautuneena käyttäjänä pystyn muokkaamaan itse luomieni korttien tekstiä (esim. kysymystä), jotta voin esimerkiksi korjata kirjoitusvirheitä tai lisätä siihen informaatiota.
* Kirjautuneena käyttäjänä pystyn muokkaamaan itse luomieni kysymysten mallivastauksia, jotta voin esimerkiksi korjata kirjoitusvirheitä tai lisätä informaatiota.
* Kirjautuneena käyttäjänä pystyn muokkaamaan itse luomieni korttien oppimisen itsearviota (mastery, mastered), jotta voin seurata edistymistäni, ja rajata kuulusteluaineistoa, keskittyen enimmäkseen vähemmän hallitsemaani materiaaliin.
* Kirjautuneena käyttäjänä pystyn poistamaan itse luomiani kortteja, mikäli olen esimerkiksi lisännyt vahingossa kaksi hyvin samanlaista korttia, tai haluan nopeasti ja radikaalisti muokata aineistoa.
* Kirjautuneena käyttäjänä voin myös paljastaa ja piilottaa mallivastauksia sekä päivittää itsearviota kysymysten listauksessa, jotta voin kätevästi kuulustella aineistoa itseltäni.

###

* Kirjautuneena käyttäjänä pystyn kirjautumaan ulos, jotta sisäänkirjautumiseni ei jää päälle, eikä esimerkiksi toinen saman koneen käyttäjä pääse käyttämään tunnuksiani luvatta.


### Järjestelmänvalvoja

* Järjestelmänvalvojana (kirjautuneena) voin muokata muiden käyttäjien aihealueita, jotta voin lisätä varoitustekstin joillekin sopimattomasta sisällöstä.
* Järjestelmänvalvojana voin poistaa muiden käyttäjien aihealueita, yrittääkseni hallita asiattomien tai liian pitkään tyhjininä seisseiden aihealueiden kertymistä sovellukseen.
* Järjestelmänvalojana voin muokata muiden käyttäjien kysymyskortteja, jotta voin esimerkiksi sensuroida asiatonta sisältöä, ja jättää kommentin "(Asiaton sisältö sensuroitu. -admin)".
* Järjestelmänvalvojana voin poistaa muiden käyttäjien kortteja, sensuroidakseni asiatonta sisältöä nopeasti ja radikaalisti.

###

* Järjestelmänvalvojana pystyn listaamaan kaikki käyttäjät ja heidän käyttäjäroolinsa, jotta pysyn kartalla käyttäjien määrästä, ylläpitäjien määrästä, sekä siitä, kenellä on järjestelmänvalvojan oikeudet.
  ```
  SELECT a.username, r.name FROM account a
  LEFT JOIN Role r 
  ON a.id IN (SELECT account_id FROM user_roles ur 
  WHERE ur.account_id = a.id AND ur.role_id = r.id)
  GROUP BY r.name, a.username;
  ```