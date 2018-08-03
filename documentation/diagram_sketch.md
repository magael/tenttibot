| User |  |
| --- | --- |
| id (primary key) | Integer |
| username | String |
| password | Integer |
| material | List(Material) |

User <-- 1 to * --> Material

| Material |  |
| --- | --- |
| id (primary key) | Integer |
| questions | List(Question) |

Material <-- 1 to * --> Question

| Question |  |
| --- | --- |
| id (primary key) | Integer |
| date_created | db.DateTime |
| date_modified | db.DateTime |
| name | String |
| sample_answer | String |
| current_answer | String |
| mastered (advanced version: grade)| Boolean (adv.: Integer) |
