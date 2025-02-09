select s.name, t.fullname
from subjects as s
join teachers t on t.id = s.teacher_id
where t.fullname = 'пані Світлана Демʼяненко';