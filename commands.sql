CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    f_name TEXT NOT NULL,
    l_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone INTEGER,
    vat INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    sku INTEGER,
    product_name TEXT NOT NULL,
    price REAL,
    PRIMARY KEY (sku)
);

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    passw TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS orders (
    order_no INTEGER PRIMARY KEY AUTOINCREMENT,
    prod_sku INTEGER NOT NULL,
    customer_vat TEXT NOT NULL,
    order_status TEXT DEFAULT 'Fullfilled'
);