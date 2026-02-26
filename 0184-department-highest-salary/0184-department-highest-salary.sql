# Write your MySQL query statement below
select d.name As Department, e.name AS Employee, e.salary AS Salary
from Employee e
join Department d on e.departmentid = d.id
where e.salary = (
    select max(salary)
    FROM Employee
    WHERE departmentId = e.departmentId
);