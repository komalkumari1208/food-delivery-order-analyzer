USE food_delivery;
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    order_id VARCHAR(20),
    customer_id VARCHAR(20),
    restaurant_name VARCHAR(100),
    cuisine_type VARCHAR(50),
    order_date DATE,
    location VARCHAR(50),
    cost_of_the_order DECIMAL(10,2),
    rating DECIMAL(3,1),
    food_preparation_time INT,
    delivery_time INT,
    day_type VARCHAR(20),
    total_delivery_time INT
);
SHOW TABLES;
SELECT COUNT(*) AS total_orders
FROM orders;
SELECT *
FROM orders
LIMIT 10;
DESCRIBE orders;
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM orders;
SELECT 
    ROUND(SUM(cost_of_the_order), 2) AS total_revenue
FROM orders;
SELECT 
    ROUND(AVG(cost_of_the_order), 2) AS average_order_value
FROM orders;
SELECT 
    ROUND(AVG(rating), 2) AS average_rating
FROM orders;
SELECT 
    ROUND(AVG(delivery_time), 2) AS average_delivery_time
FROM orders;
SELECT
    restaurant_name,
    COUNT(*) AS total_orders,
    ROUND(SUM(cost_of_the_order), 2) AS revenue
FROM orders
GROUP BY restaurant_name
ORDER BY revenue DESC
LIMIT 10;
SELECT
    cuisine_type,
    COUNT(*) AS total_orders
FROM orders
GROUP BY cuisine_type
ORDER BY total_orders DESC;
SELECT
    location,
    COUNT(*) AS total_orders,
    ROUND(SUM(cost_of_the_order), 2) AS revenue
FROM orders
GROUP BY location
ORDER BY total_orders DESC;
SELECT
    cuisine_type,
    ROUND(AVG(delivery_time), 2) AS average_delivery_time
FROM orders
GROUP BY cuisine_type
ORDER BY average_delivery_time DESC;
SELECT
    day_type,
    COUNT(*) AS total_orders,
    ROUND(SUM(cost_of_the_order), 2) AS revenue,
    ROUND(AVG(cost_of_the_order), 2) AS average_order_value
FROM orders
GROUP BY day_type;
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    COUNT(*) AS total_orders
FROM orders
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    ROUND(SUM(cost_of_the_order), 2) AS revenue
FROM orders
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;