# Write your MySQL query statement below

select distinct num AS ConsecutiveNums
from(
    SELECT 
        num,
        LEAD(num,1) over (order by id) AS next_num,
        LEAD(num,2) over (order by id) AS third_num
    FROM logs
) t
 where num = next_num AND num = third_num;
