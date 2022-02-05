SELECT customers.name, customers.email FROM customers WHERE customers.reg < now() - INTERVAL '2 DAYS'
