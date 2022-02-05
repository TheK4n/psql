CREATE TABLE items(
    pid SERIAL PRIMARY KEY,
    uid UUID NOT NULL DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL CHECK(length(name) <= 200),
    description TEXT DEFAULT '' CHECK(length(description) <= 500),
    price NUMERIC(10,2) NOT NULL CHECK(price > 0),
    seller_pid INTEGER NOT NULL REFERENCES sellers(pid),
    amount INTEGER NOT NULL CHECK(amount >= 0)
);
