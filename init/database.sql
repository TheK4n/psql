CREATE DATABASE shop;
CREATE USER shop_admin WITH ENCRYPTED PASSWORD '1234';
GRANT ALL PRIVILEGES ON DATABASE shop TO shop_admin;
ALTER DATABASE shop OWNER TO shop_admin;
-- \c shop postgres
ALTER ROLE "shop_admin" WITH LOGIN;
-- \c shop shop_admin
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
