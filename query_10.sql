select distinct sub.name as subject, s.fullname as student, t.fullname as teacher
from grades gr
join subjects sub on sub.id = gr.subject_id
join students s on s.id = gr.student_id
join teachers t on t.id = sub.teacher_id
where s.fullname = 'Охрім Баштан' and t.fullname = 'Ірена Атрощенко';