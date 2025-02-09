select t.fullname as teacher, s.fullname as student, round(avg(gr.grade), 2) as avg_grade
from grades gr
join subjects sub on sub.id = gr.subject_id
join teachers t on t.id = sub.teacher_id
join students s on s.id = gr.student_id
where t.fullname = 'Наталія Алексійчук' and s.fullname = 'Дарина Демʼянюк'
group by teacher, student;