from db import ConnectionData, PostgreSQL
from populate_custs import populate_customers
from populate_itm import populate_items_for_many_sellers
from populate_sel import populate_sellers
import os


if __name__ == '__main__':

    host = os.environ.get("PG_HOST", "127.0.0.1")
    port = int(os.environ.get("PG_PORT", 5432))
    dbname = os.environ.get("PG_DB", "postgres")
    user = os.environ.get("PG_USER", "postgres")
    password = os.environ.get("PG_PASSWORD", "1234")

    conn_data = ConnectionData(host=host, port=port, dbname=dbname, user=user, password=password)
    db = PostgreSQL(conn_data)
    populate_customers(db)
    populate_sellers(db)
    populate_items_for_many_sellers(db)
