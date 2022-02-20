import psycopg2

from db import PostgreSQL, ConnectionData
from sql import SQL
import faker
import random


def add_seller(database, name, email):
    cursor = database.conn.cursor()
    try:
        cursor.execute(SQL.add_seller.format(name=name, email=email, balance=0))
    except psycopg2.DatabaseError as e:
        database.conn.rollback()
        cursor.close()
        print("[ERROR] Adding seller: ", name, email, 0)
        print(str(e))
    else:
        database.conn.commit()
        cursor.close()
        print("[OK] Adding seller:", name, email, 0)


def populate_sellers(database: PostgreSQL):
    fake = faker.Faker()
    for i in range(100):
        seed = random.randint(1, 1000000000000000)
        faker.Faker.seed(seed)
        user_name = fake.name()
        faker.Faker.seed(seed)
        user_email = fake.email()
        add_seller(database, user_name, user_email)


if __name__ == '__main__':

    conn_data = ConnectionData(host="127.0.0.1", port=54321, dbname="shop", user="shop_admin", password="1234")
    db = PostgreSQL(conn_data)
    populate_sellers(db)
