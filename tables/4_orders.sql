CREATE TABLE orders(
    pid SERIAL PRIMARY KEY,
    uid UUID NOT NULL DEFAULT uuid_generate_v4(),
    customer_pid INTEGER NOT NULL REFERENCES customers(pid),
    item_pid INTEGER NOT NULL REFERENCES items(pid),
    price NUMERIC(10,2) NOT NULL CHECK(price > 0),
    reg TIMESTAMP NOT NULL DEFAULT now()
);
