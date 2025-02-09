SELECT DISTINCT
    s.fullname AS student,
    sub.name AS subject
FROM
    grades gr
JOIN
    students s ON s.id = gr.student_id
JOIN
    subjects sub ON sub.id = gr.subject_id
WHERE
    s.fullname = 'Христина Бгиденко';