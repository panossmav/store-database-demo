CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    f_name TEXT NOT NULL,
    l_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone INTEGER,
    dob DATE,
    vat INTEGER,
    business BOOLEAN
);
