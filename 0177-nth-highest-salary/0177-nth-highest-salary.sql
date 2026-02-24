CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  set N = N-1;
  RETURN (

    select distinct salary
    from Employee
    Order by Salary DESC
    Limit 1 offset N

  );
END