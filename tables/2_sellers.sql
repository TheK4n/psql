CREATE TABLE sellers(
    pid SERIAL PRIMARY KEY,
    uid UUID NOT NULL DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL CHECK(length(name) <= 70),
    email TEXT NOT NULL UNIQUE CHECK(length(email) <= 100),
    balance MONEY NOT NULL DEFAULT 0 CHECK(balance >= MONEY(0)) CHECK(email ~ '^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'),
    reg DATE NOT NULL DEFAULT now()
);
