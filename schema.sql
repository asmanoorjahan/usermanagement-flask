DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    dob DATE,
    email TEXT,
    password TEXT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
