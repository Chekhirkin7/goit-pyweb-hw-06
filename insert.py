import logging
from faker import Faker
from psycopg2 import DatabaseError
from connect import create_connection
from random import randint

fake = Faker('uk-UA')

def insert_data(conn):
    c = conn.cursor()

    try:
        groups = ['Group 1', 'Group 2', 'Group 3']
        for group in groups:
            c.execute("INSERT INTO groups (name) VALUES (%s);", (group,))
        conn.commit()

        for _ in range(5):
            c.execute("INSERT INTO teachers (fullname) VALUES (%s);", (fake.name(),))
        conn.commit()

        subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Literature']
        for subject in subjects:
            c.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s);", (subject, randint(1, 5)))
        conn.commit()

        for _ in range(50):
            c.execute("INSERT INTO students (fullname, group_id) VALUES (%s, %s);", (fake.name(), randint(1, 3)))
        conn.commit()

        for student_id in range(1, 51):
            for subject_id in range(1, 9):
                for _ in range (randint(10, 20)):
                    grade = randint(50, 100)
                    grade_date = fake.date_time_this_year()
                    c.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (%s, %s, %s, %s);", (student_id, subject_id, grade, grade_date))
        conn.commit()

    except DatabaseError as err:
        logging.error(err)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    try:
        with create_connection() as conn:
            if conn is not None:
                insert_data(conn)
            else:
                print("ERROR: Connection is None")
    except RuntimeError as e:
        logging.error(e)