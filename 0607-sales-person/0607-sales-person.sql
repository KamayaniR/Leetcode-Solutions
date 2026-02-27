# Write your MySQL query statement below
select name from SalesPerson 
where sales_id NOT in
(select sales_id from Orders o join Company as c on c.com_id = o.com_id where c.name = "RED");

