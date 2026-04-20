# Write your MySQL query statement below
select u.name, coalesce(sum(r.distance),0) as travelled_distance from users u
left join Rides r on u.id = r.user_id
group by u.name , u.id
order by travelled_distance desc, u.name


