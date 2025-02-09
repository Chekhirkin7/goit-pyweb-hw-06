from psycopg2 import DatabaseError
import logging
from connect import create_connection

def create_table(conn, sql_expression):
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()

if __name__ == '__main__':

    SQL_CREATE_TABLE_GROUPS = """
        DROP TABLE IF EXISTS GROUPS;
        CREATE TABLE GROUPS (
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(50) NOT NULL
        );
    """

    SQL_CREATE_TABLE_STUDENTS = """
        DROP TABLE IF EXISTS STUDENTS;
        CREATE TABLE STUDENTS (
            ID SERIAL PRIMARY KEY,
            FULLNAME VARCHAR(150) NOT NULL,
            GROUP_ID SERIAL REFERENCES GROUPS(ID)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        );
    """

    SQL_CREATE_TABLE_TEACHERS = """
        DROP TABLE IF EXISTS TEACHERS;
        CREATE TABLE TEACHERS (
            ID SERIAL PRIMARY KEY,
            FULLNAME VARCHAR(150) NOT NULL
        );
    """

    SQL_CREATE_TABLE_SUBJECTS = """
        DROP TABLE IF EXISTS SUBJECTS;
        CREATE TABLE SUBJECTS (
            ID SERIAL PRIMARY KEY,
            NAME VARCHAR(175) NOT NULL,
            TEACHER_ID SERIAL REFERENCES TEACHERS(ID)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        );
    """

    SQL_CREATE_TABLE_GRADES = """
        DROP TABLE IF EXISTS GRADES;
        CREATE TABLE GRADES (
            ID SERIAL PRIMARY KEY,
            STUDENT_ID SERIAL REFERENCES STUDENTS(ID)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
            SUBJECT_ID SERIAL REFERENCES SUBJECTS(ID)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
            GRADE INTEGER CHECK (GRADE >= 0 AND GRADE <= 100),
            GRADE_DATE DATE NOT NULL
        );
    """


    try:
        with create_connection() as conn:
            if conn is not None:
                create_table(conn, SQL_CREATE_TABLE_GROUPS)
                create_table(conn, SQL_CREATE_TABLE_STUDENTS)
                create_table(conn, SQL_CREATE_TABLE_TEACHERS)
                create_table(conn, SQL_CREATE_TABLE_SUBJECTS)
                create_table(conn, SQL_CREATE_TABLE_GRADES)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as e:
        logging.error(e)