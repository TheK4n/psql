BEGIN;
    -- new order
    INSERT INTO orders(customer_pid, item_pid, price) VALUES(2, 3, (SELECT price FROM items WHERE pid = 3));

    -- minus item price from customer balance
    UPDATE customers SET balance = balance - (SELECT price FROM items WHERE pid = 3) WHERE pid = 2;

    -- minus one of amount item
    UPDATE items SET amount = amount - 1 WHERE pid = 3;
COMMIT;
