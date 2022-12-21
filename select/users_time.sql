SELECT customers.name, customers.email FROM customers WHERE customers.reg < now() - INTERVAL '2 DAYS'

-- Самый транжира по колличеству
SELECT name, balance FROM customers WHERE pid = (SELECT o.customer_pid FROM orders AS o GROUP BY o.customer_pid ORDER BY count(1) DESC LIMIT 1);

-- Предмет с самым большим колличеством продаж
SELECT pid, price, amount FROM items WHERE pid = (SELECT o.item_pid FROM orders AS o GROUP BY o.item_pid ORDER BY count(1) DESC LIMIT 1);

-- Продавец предмета с самым большим колличеством продаж
SELECT * FROM sellers WHERE pid = (SELECT seller_pid FROM items WHERE pid = (SELECT o.item_pid FROM orders AS o GROUP BY o.item_pid ORDER BY count(1) DESC LIMIT 1));

-- Топ продавцов по сумме продаж
SELECT s.name, sum(i.price) AS order_sums FROM orders AS o INNER JOIN items AS i ON o.item_pid = i.pid INNER JOIN sellers AS s ON i.seller_pid = s.pid GROUP BY s.name, s.uid ORDER BY sum(i.price) DESC;

-- Колличество покупок товаров у конкретного продавца конкретным покупателем
SELECT u.uid, s.uid, count(1) as interactions from customers as u inner join orders as o on u.pid = o.customer_pid inner join items as i on o.item_pid = i.pid inner join sellers as s on i.seller_pid = s.pid group by u.uid, s.uid order by interactions desc;

-- Сумма всех трат
SELECT sum(i.price) FROM items AS i INNER JOIN orders AS o ON o.item_pid = i.pid;
