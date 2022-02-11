import psycopg2

from db import PostgreSQL, ConnectionData
from sql import SQL
import faker
import random


def add_costumer(database, user_name, user_email, user_balance):
    cursor = database.conn.cursor()
    try:
        cursor.execute(SQL.add_costumer.format(name=user_name, email=user_email, balance=user_balance))
    except psycopg2.DatabaseError as e:
        database.conn.rollback()
        cursor.close()
        print("[ERROR] Adding customer: ", user_name, user_email, user_balance)
        print(str(e))
    else:
        print("[OK] Adding customer:", user_name, user_email, user_balance)
        database.conn.commit()
        cursor.close()


def populate_customers(database: PostgreSQL):
    fake = faker.Faker()
    for i in range(10000):
        seed = random.randint(1, 1000000000000000)
        faker.Faker.seed(seed)
        user_name = fake.name()
        faker.Faker.seed(seed)
        user_email = fake.email()
        user_balance = random.randint(1, 1000)
        add_costumer(database, user_name, user_email, user_balance)


if __name__ == '__main__':

    conn_data = ConnectionData(host="127.0.0.1", port=54321, dbname="shop", user="shop_admin", password="1234")
    db = PostgreSQL(conn_data)
    populate_customers(db)
