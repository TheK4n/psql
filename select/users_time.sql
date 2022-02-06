SELECT customers.name, customers.email FROM customers WHERE customers.reg < now() - INTERVAL '2 DAYS'

-- Колличество продаж у самого богатого продавца
SELECT count(*) FROM orders WHERE seller_pid = (SELECT pid FROM sellers WHERE balance > 0 ORDER BY balance DESC LIMIT 1);
