
SELECT 
    o.OrderID,
    o.CustomerID,
    o.EmployeeID,
    eo.EmployeeOrderCount,
    o.OrderDate
FROM 
    Orders o
INNER JOIN 
    (SELECT 
        EmployeeID, 
        COUNT(OrderID) AS EmployeeOrderCount
     FROM Orders
     GROUP BY EmployeeID) eo
ON o.EmployeeID = eo.EmployeeID;


SELECT
    p.ProductID,
    p.ProductName,
    c.CategoryName,
    COUNT(p.ProductID) OVER (PARTITION BY p.CategoryID) -1 AS 'Other Products in Same Category'
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID;


SELECT DISTINCT
    p.ProductID,
    p.ProductName,
    c.CategoryName,
    SUM(od.Quantity) OVER (PARTITION BY p.CategoryID) as 'Total Units on Order for Category'
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
JOIN OrderDetails od ON p.ProductID = od.ProductID


SELECT
    OrderID,
    CustomerID,
    OrderDate,
    RANK() OVER (PARTITION BY CustomerID ORDER BY OrderDate) AS 'Order Rank for Customer'
From Orders



SELECT
    OrderID,
    OrderDate,
    Freight,
    LAG(Freight) OVER (ORDER BY OrderDate) AS 'Previous Order Freight'
From Orders;


DROP TABLE IF EXISTS Temp;

WITH FirstOrderDate (CustomerID,FirstOrder)
AS
(
    SELECT CustomerID,
    FIRST_VALUE(OrderDate) OVER (PARTITION BY CustomerID ORDER BY OrderDate) AS FirstOrder
    FROM Orders
)


SELECT
    o.OrderID,
    o.CustomerID,
    o.EmployeeID,
    o.OrderDate,
    fo.FirstOrder
INTO Temp
FROM Orders o
JOIN FirstOrderDate fo ON o.CustomerID = fo.CustomerID 

SELECT DISTINCT
    OrderID,
    CustomerID,
    EmployeeID,
    OrderDate,
    DATEDIFF(DAY,FirstOrder, OrderDate) AS 'Days Since First Order'
From Temp
ORDER BY OrderID 


DROP TABLE IF EXISTS Temp2;

SELECT
    o.OrderID,
    (od.UnitPrice * od.Quantity)*(1-od.Discount) AS TotalPrice,
    o.OrderDate
INTO Temp2
FROM Orders o
JOIN OrderDetails od ON o.OrderID = od.OrderID

SELECT 
    OrderID,
    TotalPrice,
    OrderDate,
    AVG(TotalPrice) OVER (ORDER BY OrderDate ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING) as '5-Point Moving Average of Total Price'
From Temp2