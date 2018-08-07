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

| UserMaterial | |
| --- | --- |
| (fk) user_id | Integer |
| (fk) material_id | Integer |

UserMaterial * to 1 Material

| Material |  |
| --- | --- |
| (pk) id | Integer |

Material 1 to * Question

| Question |  |
| --- | --- |
| (pk) id | Integer |
| date_created | DateTime |
| date_modified | DateTime |
| name | String |
| sample_answer | String |
| current_answer | String |
| mastered (advanced version: grade)| Boolean (adv.: Integer) |
| (fk) material | Material |
(oisko parempi vaan et "material" -> kyssärin "topic"-attribuutti eikä taulu?)
(mites "current" vastaus, oma taulu?)
