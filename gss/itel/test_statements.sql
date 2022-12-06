DROP DATABASE IF EXISTS north_telco;
CREATE DATABASE north_telco;

USE north_telco;

DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS consumes;


CREATE TABLE customers(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(50) NOT NULL
);

CREATE TABLE consumes(
    consume_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    customer_id INT UNSIGNED NOT NULL,
    daily_consume INT DEFAULT 0,
    consume_date DATETIME DEFAULT current_timestamp,
    FOREIGN KEY (customer_id) REFERENCES customers (id)
);

--Get gruped data from consumes using a view
CREATE VIEW monthly_consume_vw AS 
SELECT consumes.customer_id,
       SUM(consumes.daily_consume) AS consume,
       MONTH(consume_date) as months
FROM consumes
GROUP BY consumes.customer_id, months;

--Use the view to get the customer_id with more consume
SELECT customer_id FROM monthly_consume_vw
WHERE months = 11
ORDER BY consume DESC
LIMIT 1;


--Ranked consumed data
CREATE VIEW daily_consume_rank_vw AS
SELECT *,
    DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY daily_consume DESC) AS my_rank
FROM consumes;

--Top 3 consumption dates for each customer
SELECT customer_id, daily_consume, consume_date, customer_name FROM daily_consume_rank_vw
JOIN customers
ON customers.id = daily_consume_rank_vw.customer_id
WHERE my_rank <= 3;