DROP TABLE IF EXISTS first_names;

CREATE TABLE first_names(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT not NULL,
    nationality TEXT not NULL
);