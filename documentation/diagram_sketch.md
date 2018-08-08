| User |  |
| --- | --- |
| (pk) id | Integer |
| name | String|
| username | String |
| password | String |
| date_created | DateTime |
| date_modified | DateTime |

(User * to * Subject)

User 1 to * UserSubject 

| UserSubject |  |
| --- | --- |
| (fk) user_id | Integer |
| (fk) subject_id | Integer |

UserSubject * to 1 Subject

| Subject |  |
| --- | --- |
| (pk) id | Integer |
| date_created | DateTime |
| date_modified | DateTime |

Subject 1 to * Question

| Question |  |
| --- | --- |
| (pk) id | Integer |
| date_created | DateTime |
| date_modified | DateTime |
| name | String |
| sample_answer | String |
| latest_answer | String |
| mastered (advanced version: grade / mastery)| Boolean (adv.: Integer) |
| (fk) subject_id | Subject |

* Mites "latest" vastaus, oma taulu?
* Entä muut kohdat, joita ei välttämättä haluta jakaa: mallivastaus, itsearvio?
* "private" aineisto boolean?
