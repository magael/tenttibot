
Alkuperäisen admin-roolin lisääminen:

1. Rekisteröidy sovelluksessa, esimerkiksi nimimerkillä admin.

2. Syötä komentokehotteesa, sovelluksen juuressa komento:
    sqlite3 application/questions.db

3. Lisätäksesi admin-roolin "admin"-nimiselle käyttäjälle syötä seuraava SQL-kysely:

UPDATE Role SET name = 'ADMIN' WHERE Role.id IN (SELECT id FROM account WHERE account.name = 'admin');

4. Nyt admin-rooli on lisätty valitsemallesi käyttäjälle. Voit varmistaa asian esimerkiksi listaamalla kaikkien käyttäjien roolit kyselyllä

SELECT a.username, r.name FROM account a LEFT JOIN Role r ON a.id IN (SELECT account_id FROM user_roles ur WHERE ur.account_id = a.id AND ur.role_id = r.id) GROUP BY a.username;