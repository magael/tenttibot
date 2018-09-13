# Jatkokehitysideoita

### Omien ja muiden aihealueiden listaus erikseen

* Etusivulle "My Subjects" -listaus
  * Esim. 10 viimeisintä ja linkki kaikkien omien listaukseen
  * Yläpalkkiin linkki kaikkien omien listaukseen
* Etusivulle 10 viimeksi muokattua aihealuetta ja linkki kaikkien aihealueiden listaukseen

### Kuulustelutaulu ja -näkymä

Alkuperäisen tarkoituksen mukainen kuulustelunäkymä jäi ajanpuutteen vuoksi toteuttamatta loppupalautukseen. Kuvaus suunnitelmasta:

Kysymyksen listauksessa linkki uuteen kuulusteluun, jossa samassa, tai kuulustelunaloitusnäkymä-kaavakkeessa asetetaan aineiston rajaus, esim. "mastery < 4".

Kysymyskortteja kuulustellaan yksitellen, satunnaisessa järjestyksessä, kunnes pakka on kertaalleen käyty läpi.

Joka kysymyksen kohdalla on muutoin nykyisen kaltainen korttinäkymä, mutta siinä on lisäksi kenttä, johon vastaus syötetään. Vastauksen (saa olla myös tyhjä) jätettyään (napin painauksella / Enterillä) käyttäjälle paljastuu mallivastaus, ja hän voi päivittää itsearvion.

Kun pakka on käyty läpi, kysytään uuden kuulustelun aloittamisesta uudella rajauksella, esimerkiksi edellä mainitulla kaavakkeella.

Lisäksi voisi olla näkymä kunkin kuulustelun lopputuloksesta: tilastoja oppimisen etenemisestä.

Toteutusta varten luonnostellut tietokantataulut:

**Quiz**

id

date_created

(fk) user_id

**QuizQuestions**

(pk/fk) quiz_id

(pk/fk) question_id

answer: String

mastery_before: Integer

mastery_after: Integer

### Jakaminen

* Subjectiin password-attribuutti.
* Mikäli salasanan jättää tyhjäksi, aineisto on julkinen, muuten yksityinen.
* Listataan / merkitään erikseen yksityiset ja julkiset aineistot.
* Yksityisten aineistojen kohdalla, mikäli käyttäjällä ei ole yhteyttä aineistoon user_subjects:issa, näytetään kysymysten listauksen sijaan ensin lomake, jossa voi syöttää salasanan.
* Jos salasana on oikea, luodaan yhteys user_subjects:iin.

### Muita

* reps(repetitions)-muuttuja kortteihin (ja graduation)

* Käyttöohjeet ajan tasalle

* Mastery ehkä table eikä db.model

* Sivutus

* (valinnaiset) koulutustaso, organisaatio, oppiaine -yläkategoriat

* Mahdollisia uusia käyttäjärooleja voisi olla esim. opettaja, esimerkkilukion opettaja

* Monivalintamoodi

* (actual)koe-moodi

* Harjotuskoemoodi, missä valitaan randomilla aineistosta kysymyksiä tietyn pistemäärän täyttämiseksi. pisteiden perusteella arvosana

* Salasanan bruteforceyritys johtaa aikalukkoon

* Info for students, for educators, oppimisesta, käyttöohje, about

* Admin voi muokkata käyttäjien rooleja

* Admin voi poistaa käyttäjiä (samalla kaikki sen aineistot)

* Adminille users-linkki navbariin

* HTML-elementtien nimeäminen ym. accessibility

* Suosikki-subjectien lisäys

* List subjectit joissa (kirjautunut käyttäjä itse) on viimeksi muokannut masterya

* Herokun kaatuilun fiksaus

* Aineistojen (Subject) muokkausoikeuksien jakaminen käyttäjien välillä
* Aineistoista kopioiden luominen (jotta voi lisätä ja muokata oman kopioonsa kysymyskortteja)
* Aihealueisiin liittyvät avainsanat, "tagit" ja selailu niiden perusteella
* Hakutoiminnallisuuksia
* Nimenmuutoksia enemmän "flash cards" -tyylisiksi
* Kuvien lisäys "kortteihin"
* Muistiinpanot (aihe- ja/tai kysymyskohtaiset)
* Julkisten aineistojen kommentointi
* Algoritmi, joka päättää, milloin minkäkin arvosanan saanut kysymys kysytään uudestaan (vaihtoehtona käyttäjän itse rajaamaan aineistoon)
* Mahdollisuus aineistojen tallentamiseen paikallisesti (ehkä myös tulostukseen sopivassa muodossa) (+ ehkä muokkaus ja lataus takaisin)
* Työpöytäsovellus
* Käyttöliittymä usealle kielelle
* Käyttäjätunnuksen vahvistaminen sähköpostilla ym. "turvallisuuden" kehittämistä
* find_author-kysely: Add date_created & -modified to user_subjects and order this query by us.date_created
* auth_register()-funktion pilkkominen pienemmiksi funktioiksi