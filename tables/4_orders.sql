CREATE TABLE orders(
    pid SERIAL PRIMARY KEY,
    uid UUID NOT NULL DEFAULT uuid_generate_v4(),
    customer_pid INTEGER NOT NULL REFERENCES customers(pid),
    item_pid INTEGER NOT NULL REFERENCES items(pid),
    reg TIMESTAMP NOT NULL DEFAULT now()
);
