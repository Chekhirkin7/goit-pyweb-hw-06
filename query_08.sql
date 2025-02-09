select t.fullname as teacher, s.name as subject, round(AVG(gr.grade), 2) as aver_grade
from grades gr
join subjects s on s.id = gr.subject_id
join teachers t on t.id = s.teacher_id
where t.fullname = 'Наталія Алексійчук'
group by teacher , subject;