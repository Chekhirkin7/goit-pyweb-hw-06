select s.fullname, g.name
from students as s
join groups g on g.id = s.group_id
where g.name = 'Group 1';