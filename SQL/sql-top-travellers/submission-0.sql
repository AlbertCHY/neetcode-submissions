-- Write your query below
select u.name, coalesce(sum(r.distance), 0) AS travelled_distance
from users u
LEFT JOIN rides r ON u.id = r.user_id
GROUP BY u.id, u.name
order by travelled_distance desc, name asc;