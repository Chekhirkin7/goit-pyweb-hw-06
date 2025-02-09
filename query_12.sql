select s.fullname as student, sub.name as subject, g.name as group, gr.grade, gr.grade_date
from grades gr
join students s on s.id = gr.student_id
join subjects sub on sub.id = gr.subject_id
join groups g on g.id = s.group_id
where sub.name = 'Math' and g.name = 'Group 1' and grade_date = (
	select max(grade_date)
	from grades
	where subject_id = sub.id
)
order by student;