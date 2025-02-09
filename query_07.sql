select gr.grade, g.name as group_name, s.fullname as student_name, s2.name as subject
from grades gr
join students s on s.id = gr.student_id
join subjects s2 on s2.id = gr.subject_id
join groups g on g.id = s.group_id
where s2.name = 'Math' and g.name = 'Group 1'
order by group_name, student_name;