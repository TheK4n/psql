
import psycopg2

from db import PostgreSQL, ConnectionData
from sql import SQL


def get_random_customer(database):
    cursor = database.conn.cursor()
    cursor.execute(SQL.get_random_customer_pid)
    return cursor.fetchone()[0]


def get_random_item(database):
    cursor = database.conn.cursor()
    cursor.execute(SQL.get_random_item_pid)
    return cursor.fetchone()[0]


def commit_transaction(database, customer_pid, item_pid):
    cursor = database.conn.cursor()
    try:
        cursor.execute(SQL.transaction_buy.format(item_pid=item_pid, customer_pid=customer_pid))
    except psycopg2.DatabaseError as e:
        database.conn.rollback()
        cursor.close()
        print(str(e))
        print("[ERROR] Committing transaction: ", item_pid, customer_pid)
    else:
        print("[OK] Committing transaction:", item_pid, customer_pid)
        database.conn.commit()
        cursor.close()


if __name__ == '__main__':
    conn_data = ConnectionData(host="127.0.0.1", port=54321, dbname="shop", user="shop_admin", password="1234")
    db = PostgreSQL(conn_data)
    for i in range(1000):
        commit_transaction(db, get_random_customer(db), get_random_item(db))
