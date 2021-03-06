CREATE TABLE polls (
    id SERIAL PRIMARY KEY,
    topic TEXT,
    created_at TIMESTAMP
);
CREATE TABLE choices (
    id SERIAL PRIMARY KEY,
    poll_id INTEGER REFERENCES polls,
    choice TEXT
);
CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    choice_id INTEGER REFERENCES choices,
    sent_at TIMESTAMP
);
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    admin TEXT,
    occupation TEXT
);
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    poll_id INTEGER REFERENCES polls,
    content TEXT,
    username TEXT,
    created_at TIMESTAMP
);
CREATE TABLE fights (
    id SERIAL PRIMARY KEY,
    fight TEXT
);
CREATE TABLE recommendations (
    id SERIAL PRIMARY KEY,
    poll_id INTEGER REFERENCES polls,
    occupation TEXT
);