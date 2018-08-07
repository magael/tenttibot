| User |  |
| --- | --- |
| (pk) id | Integer |
| name | String|
| username | String |
| password | String |
| date_created | DateTime |
| date_modified | DateTime |

(User * to * Material)

User 1 to * UserMaterial 

| UserMaterial |  |
| --- | --- |
| (fk) user_id | Integer |
| (fk) material_id | Integer |

UserMaterial * to 1 Material

| Material |  |
| --- | --- |
| (pk) id | Integer |
| date_created | DateTime |
| date_modified | DateTime |

Material 1 to * Question

| Question |  |
| --- | --- |
| (pk) id | Integer |
| date_created | DateTime |
| date_modified | DateTime |
| name | String |
| sample_answer | String |
| latest_answer | String |
| mastered (advanced version: grade)| Boolean (adv.: Integer) |
| (fk) material | Material |

* Oisko parempi vaan et "material" -> kyssärin "topic"-attribuutti eikä taulu?
* Mites "latest" vastaus, oma taulu?
* Entä muut kohdat, joita ei välttämättä haluta jakaa: mallivastaus, itsearvio?
* "private" aineisto boolean?
