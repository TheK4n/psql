from db import ConnectionData, PostgreSQL
from populate_custs import populate_customers
from populate_itm import populate_items_for_many_sellers
from populate_sel import populate_sellers

if __name__ == '__main__':

    conn_data = ConnectionData(host="127.0.0.1", port=54321, dbname="shop", user="shop_admin", password="1234")
    db = PostgreSQL(conn_data)
    populate_customers(db)
    populate_sellers(db)
    populate_items_for_many_sellers(db)
