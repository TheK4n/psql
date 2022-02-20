import psycopg2

from db import PostgreSQL, ConnectionData
from sql import SQL
import faker
import random


def add_item(database, name, price, seller_pid, amount):
    cursor = database.conn.cursor()
    try:
        cursor.execute(SQL.add_item.format(name=name, price=price, seller_pid=seller_pid, amount=amount))
    except psycopg2.DatabaseError as e:
        database.conn.rollback()
        cursor.close()
        print("[ERROR] Adding item: ", name, price, seller_pid, amount)
        print(str(e))
    else:
        database.conn.commit()
        cursor.close()
        print("[OK] Adding item:", name, price, seller_pid, amount)


def populate_items_for_seller(database: PostgreSQL, seller_pid):
    fake = faker.Faker()
    for i in range(100):
        seed = random.randint(1, 1000000000000000)
        faker.Faker.seed(seed)
        name = fake.text()
        faker.Faker.seed(seed)
        price = random.randint(1, 100) + float(random.randint(0, 100) / 100.0)
        amount = random.randint(3, 25)
        add_item(database, name, price, seller_pid, amount)


def populate_items_for_many_sellers(database):
    for i in range(10):
        cursor = database.conn.cursor()
        cursor.execute(SQL.get_random_seller_pid)
        seller_pid = cursor.fetchone()[0]
        populate_items_for_seller(database, seller_pid)


if __name__ == '__main__':

    conn_data = ConnectionData(host="127.0.0.1", port=54321, dbname="shop", user="shop_admin", password="1234")
    db = PostgreSQL(conn_data)
    populate_items_for_many_sellers(db)
