CREATE TABLE IF NOT EXISTS main_course (
    generated_id INTEGER NOT NULL PRIMARY KEY,
    dish_name TEXT NOT NULL,
    popularity INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS salat (
        generated_id INTEGER NOT NULL PRIMARY KEY,
    dish_name TEXT NOT NULL,
    popularity INTEGER NOT NULL
);