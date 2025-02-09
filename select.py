import logging
from psycopg2 import DatabaseError
from connect import create_connection

if __name__ == '__main__':

    sql_select_01 = """
        SELECT s.id, s.fullname, ROUND(AVG(g.grade), 2) AS avg_grade FROM students s
        JOIN grades g ON s.id = g.student_id
        GROUP BY s.id
        ORDER BY avg_grade DESC
        LIMIT 5;
    """

    sql_select_02 = """
        SELECT s.id, s.fullname, ROUND(AVG(g.grade), 2) AS average_grade FROM grades g
        JOIN students s ON s.id = g.student_id
        where g.subject_id = 1
        GROUP BY s.id
        ORDER BY average_grade DESC
        LIMIT 1;
    """

    sql_select_03 = """
        select sub.id as subject_id, sub.name as subject_name, g.id as group_id, g.name as group_name, ROUND(AVG(gr.grade)) as aver_grade
        from grades gr
        join subjects sub on sub.id = gr.subject_id
        join students s on s.id = gr.student_id
        join groups g on g.id = s.group_id
        where sub.name = 'Math'
        group by sub.id, sub.name, g.id, g.name;
    """

    sql_select_04 = """
        select round(avg(grade), 2) as avg_grade
        from grades;
    """

    sql_select_05 = """
        select s.name, t.fullname
        from subjects as s
        join teachers t on t.id = s.teacher_id
        where t.fullname = 'пані Світлана Демʼяненко';
    """

    sql_select_06 = """
        select s.fullname, g.name 
        from students as s
        join groups g on g.id = s.group_id
        where g.name = 'Group 1';
    """

    sql_select_07 = """
        select gr.grade, g.name as group_name, s.fullname as student_name, s2.name as subject
        from grades gr
        join students s on s.id = gr.student_id 
        join subjects s2 on s2.id = gr.subject_id 
        join groups g on g.id = s.group_id 
        where s2.name = 'Math' and g.name = 'Group 1'
        order by group_name, student_name;
    """

    sql_select_08 = """
        select t.fullname as teacher, s.name as subject, round(AVG(gr.grade), 2) as aver_grade
        from grades gr
        join subjects s on s.id = gr.subject_id 
        join teachers t on t.id = s.teacher_id 
        where t.fullname = 'Наталія Алексійчук'
        group by teacher , subject;
    """

    sql_select_09 = """
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
    """

    sql_select_10 = """
        select distinct sub.name as subject, s.fullname as student, t.fullname as teacher
        from grades gr
        join subjects sub on sub.id = gr.subject_id 
        join students s on s.id = gr.student_id 
        join teachers t on t.id = sub.teacher_id 
        where s.fullname = 'Охрім Баштан' and t.fullname = 'Ірена Атрощенко';
    """

    sql_select_11 = """
        select t.fullname as teacher, s.fullname as student, round(avg(gr.grade), 2) as avg_grade
        from grades gr
        join subjects sub on sub.id = gr.subject_id
        join teachers t on t.id = sub.teacher_id
        join students s on s.id = gr.student_id
        where t.fullname = 'Наталія Алексійчук' and s.fullname = 'Дарина Демʼянюк'
        group by teacher, student;
    """

    sql_select_12 = """
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
    """

    try:
        with create_connection() as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    c.execute(sql_select_01)
                    c.execute(sql_select_02)
                    c.execute(sql_select_03)
                    c.execute(sql_select_04)
                    c.execute(sql_select_05)
                    c.execute(sql_select_06)
                    c.execute(sql_select_07)
                    c.execute(sql_select_08)
                    c.execute(sql_select_09)
                    c.execute(sql_select_10)
                    c.execute(sql_select_11)
                    c.execute(sql_select_12)
                except DatabaseError as err:
                    logging.error(err)
                finally:
                    c.close()
            else:
                print("ERROR: Connection is None")
    except RuntimeError as err:
        logging.error(err)