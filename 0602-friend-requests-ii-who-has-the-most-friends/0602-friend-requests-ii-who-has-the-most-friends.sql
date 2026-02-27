# Write your MySQL query statement below

select id, count(id) As num
from(select requester_id as id from RequestAccepted
union all 
select accepter_id as id from RequestAccepted) as t
group by id order by num desc limit 1;