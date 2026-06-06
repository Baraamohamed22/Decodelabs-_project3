-- DecodeLabs Data Analytics Project 3
-- SQL Data Analysis queries.
-- Table name: orders

-- 01. SELECT: Preview the first 10 orders.
SELECT
    OrderID,
    Date,
    CustomerID,
    Product,
    Quantity,
    UnitPrice,
    TotalPrice
FROM orders
LIMIT 10;

-- 02. WHERE: Orders with high total price.
SELECT
    OrderID,
    Date,
    Product,
    Quantity,
    UnitPrice,
    TotalPrice
FROM orders
WHERE TotalPrice >= 3000
ORDER BY TotalPrice DESC;

-- 03. ORDER BY: Top 10 orders by total revenue.
SELECT
    OrderID,
    Date,
    Product,
    Quantity,
    TotalPrice
FROM orders
ORDER BY TotalPrice DESC
LIMIT 10;

-- 04. GROUP BY with COUNT, SUM, AVG: Product performance.
SELECT
    Product,
    COUNT(*) AS OrderCount,
    SUM(Quantity) AS UnitsSold,
    ROUND(SUM(TotalPrice), 2) AS TotalRevenue,
    ROUND(AVG(TotalPrice), 2) AS AverageOrderValue
FROM orders
GROUP BY Product
ORDER BY TotalRevenue DESC;

-- 05. GROUP BY: Revenue by order status.
SELECT
    OrderStatus,
    COUNT(*) AS OrderCount,
    ROUND(SUM(TotalPrice), 2) AS TotalRevenue,
    ROUND(AVG(TotalPrice), 2) AS AverageOrderValue
FROM orders
GROUP BY OrderStatus
ORDER BY OrderCount DESC;

-- 06. WHERE and GROUP BY: Delivered orders by product.
SELECT
    Product,
    COUNT(*) AS DeliveredOrders,
    ROUND(SUM(TotalPrice), 2) AS DeliveredRevenue
FROM orders
WHERE OrderStatus = 'Delivered'
GROUP BY Product
ORDER BY DeliveredRevenue DESC;

-- 07. GROUP BY: Payment method analysis.
SELECT
    PaymentMethod,
    COUNT(*) AS OrderCount,
    ROUND(SUM(TotalPrice), 2) AS TotalRevenue,
    ROUND(AVG(TotalPrice), 2) AS AverageOrderValue
FROM orders
GROUP BY PaymentMethod
ORDER BY OrderCount DESC;

-- 08. GROUP BY: Monthly revenue trend.
SELECT
    SUBSTR(Date, 1, 7) AS YearMonth,
    COUNT(*) AS OrderCount,
    SUM(Quantity) AS UnitsSold,
    ROUND(SUM(TotalPrice), 2) AS TotalRevenue,
    ROUND(AVG(TotalPrice), 2) AS AverageOrderValue
FROM orders
GROUP BY SUBSTR(Date, 1, 7)
ORDER BY YearMonth;

-- 09. HAVING: Products with more than 170 orders.
SELECT
    Product,
    COUNT(*) AS OrderCount,
    ROUND(SUM(TotalPrice), 2) AS TotalRevenue
FROM orders
GROUP BY Product
HAVING COUNT(*) > 170
ORDER BY OrderCount DESC;

-- 10. Aggregation summary for the full dataset.
SELECT
    COUNT(*) AS TotalOrders,
    COUNT(DISTINCT CustomerID) AS UniqueCustomers,
    SUM(Quantity) AS TotalUnitsSold,
    ROUND(SUM(TotalPrice), 2) AS TotalRevenue,
    ROUND(AVG(TotalPrice), 2) AS AverageOrderValue,
    ROUND(MIN(TotalPrice), 2) AS MinimumOrderValue,
    ROUND(MAX(TotalPrice), 2) AS MaximumOrderValue
FROM orders;
