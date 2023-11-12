SELECT couriers.login, COUNT(orders.*)
FROM "Couriers" as couriers
    LEFT OUTER JOIN "Orders" as orders
        ON couriers.id = orders."courierId"
WHERE orders."inDelivery" IS TRUE
GROUP BY couriers.login

inDelivery






SELECT couriers.login, COUNT(orders.*)
FROM "Couriers" as couriers
    FULL OUTER JOIN "Orders" as orders
        ON couriers.id = orders."courierId"
WHERE orders."inDelivery" IS TRUE
GROUP BY couriers.id


SELECT couriers.login, orders.id
FROM "Couriers" as couriers
    FULL OUTER JOIN "Orders" as orders
        ON couriers.id = orders."courierId"
WHERE orders."inDelivery" = TRUE
GROUP BY couriers.id

SELECT "Couriers".login
FROM "Couriers"
    FULL OUTER JOIN "Orders"
        ON "Couriers".id = "Orders"."courierId"
WHERE "Orders"."inDelivery" = TRUE

SELECT couriers.login, coalesce(COUNT(orders."inDelivery"), 0)
FROM "Couriers" as couriers
    LEFT JOIN "Orders" as orders
        ON couriers.id = orders."courierId"
GROUP BY couriers.login




SELECT
    track,
    CASE
        WHEN (finished IS TRUE) AND ("Orders.canсelled" IS FALSE) AND ("inDelivery" IS FALSE)
            THEN 2
        WHEN (canсelled IS TRUE) AND (finished IS FALSE) AND ("inDelivery" IS FALSE)
                    THEN -1
        WHEN ("inDelivery" IS TRUE) AND (finished IS FALSE) AND (canсelled IS FALSE)
                    THEN 1
        ELSE 0
    END as order_status
FROM "Orders"


SELECT
    track,
    CASE
        WHEN (finished IS TRUE)
            THEN 2
        WHEN (cancelled IS TRUE)
                    THEN -1
        WHEN ("inDelivery" IS TRUE)
                    THEN 1
        ELSE 0
    END as order_status
FROM "Orders"