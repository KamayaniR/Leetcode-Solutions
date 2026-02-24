# Write your MySQL query statement below
Select (Select distinct salary 
from Employee
Order by salary DESC
LIMIT 1 OFFSET 1) AS SecondHighestSalary; 