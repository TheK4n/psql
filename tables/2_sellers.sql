CREATE TABLE sellers(
    pid SERIAL PRIMARY KEY,
    uid UUID NOT NULL DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL CHECK(length(name) <= 70),
    email TEXT NOT NULL UNIQUE CHECK(length(email) <= 100),
    reg DATE NOT NULL DEFAULT now()
);
