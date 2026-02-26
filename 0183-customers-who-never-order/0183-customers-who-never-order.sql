# Write your MySQL query statement below

select name AS Customers from Customers
left join Orders On Customers.id = Orders.customerId
where Orders.customerid is NULL;

