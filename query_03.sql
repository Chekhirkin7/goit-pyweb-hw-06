select sub.id as subject_id, sub.name as subject_name, g.id as group_id, g.name as group_name, ROUND(AVG(gr.grade)) as aver_grade
from grades gr
join subjects sub on sub.id = gr.subject_id
join students s on s.id = gr.student_id
join groups g on g.id = s.group_id
where sub.name = 'Math'
group by sub.id, sub.name, g.id, g.name;