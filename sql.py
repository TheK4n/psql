class SQL:
    transaction_buy = """
BEGIN;
    -- new order
    INSERT INTO orders(customer_pid, item_pid) VALUES(%(customer_pid)s, %(item_pid)s);

    -- minus item price from customer balance
    UPDATE customers SET balance = balance - (SELECT price FROM items WHERE pid = %(item_pid)s FOR SHARE) WHERE pid = %(customer_pid)s;

    -- add item price to seller balance if item belongs to seller
    UPDATE sellers SET balance = balance + (SELECT price FROM items WHERE pid = %(item_pid)s FOR SHARE) WHERE pid = (SELECT seller_pid FROM items WHERE pid = %(item_pid)s);

    -- minus one of amount item
    UPDATE items SET amount = amount - 1 WHERE pid = %(item_pid)s;
COMMIT;
"""
    add_costumer = """
INSERT INTO customers(name, email, balance, password) VALUES(%(name)s, %(email)s, %(balance)s, %(password)s);
"""
    add_item = """
INSERT INTO items(name, price, seller_pid, amount) VALUES(%(name)s, %(price)s, %(seller_pid)s, %(amount)s);
"""
    add_seller = """
INSERT INTO sellers(name, email, balance) VALUES(%(name)s, %(email)s, %(balance)s);
"""

    get_random_seller_pid = """
SELECT pid FROM sellers ORDER BY random() LIMIT 1;
"""
    get_random_item_pid = """
SELECT pid FROM items ORDER BY random() LIMIT 1;
"""
    get_random_customer_pid = """
SELECT pid FROM customers ORDER BY random() LIMIT 1;
"""
