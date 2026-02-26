# Write your MySQL query statement below

Select e2.name AS Employee 
From employee E1
INNER JOIN employee E2 on E1.id = E2.managerId
where E1.salary < E2. salary
