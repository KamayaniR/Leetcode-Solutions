# Write your MySQL query statement below


SELECT b.unique_id as unique_id , a.name as name from Employees a left join EmployeeUNI as b
on a.id = b.id
