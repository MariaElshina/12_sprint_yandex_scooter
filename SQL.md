# Выводим список курьеров с количеством их заказов в статусе "В доставке"
SELECT c.login,
	     COUNT(o.track) AS “inDelivery”
FROM “Orders” AS o
JOIN “Couriers” AS c ON o.”courierId” = c.id
WHERE o.”inDelivery” = true
GROUP BY c.login;

# Выводим все трекеры заказов и их статусы
SELECT track,
	     CASE
		    WHEN finished = true THEN 2
		    WHEN cancelled = true THEN -1
		    WHEN “inDelivery” = true THEN 1
		    ELSE 0
	     END AS status
FROM “Orders”;
