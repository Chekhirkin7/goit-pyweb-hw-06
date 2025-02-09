import psycopg2
from contextlib import contextmanager

@contextmanager
def create_connection():
    try:
        """create a database connection to database"""
        conn = psycopg2.connect(host="localhost", database="goit-pyweb-hw-06", user="postgres", password="567234")
        yield conn
        conn.close()
    except psycopg2.OperationalError as e:
        raise RuntimeError(f"Failed to create database connection {e}")
