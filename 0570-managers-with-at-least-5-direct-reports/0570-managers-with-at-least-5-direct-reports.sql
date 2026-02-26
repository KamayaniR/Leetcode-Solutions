# Write your MySQL query statement below

select e.name from Employee e
JOIN (select managerId, Count(*) as directReports
from Employee
group by managerId
having count(*) >= 5) e1 on e.id = e1.managerid;