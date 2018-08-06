| User |  |
| --- | --- |
| id (primary key) | Integer |
| name | String|
| username | String |
| password | String |
| date_created | DateTime |
| date_modified | DateTime |

User <-- * to * --> Material

| Material |  |
| --- | --- |
| id (primary key) | Integer |
| questions |
| users | List(Users) |

Material <-- 1 to * --> Question

| Question |  |
| --- | --- |
| id (primary key) | Integer |
| date_created | DateTime |
| date_modified | DateTime |
| name | String |
| sample_answer | String |
| current_answer | String |
| mastered (advanced version: grade)| Boolean (adv.: Integer) |
| material | Material |
