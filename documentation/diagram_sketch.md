| User |  |
| --- | --- |
| id (primary key) | Integer |
| username | String |
| password | Integer |
| material | List(Material) |

<- 1 --- * ->

| Material |  |
| --- | --- |
| id (primary key) | Integer |
| questions | List(Question) |

<- 1 --- * ->

| Question |  |
| --- | --- |
| id (primary key) | Integer |
| date_created | db.DateTime |
| date_modified | db.DateTime |
| name | String |
| mastered (advanced version: grade)| Boolean (adv.: Integer) |
