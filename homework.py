import sqlite3
from contextlib import closing

def get_connection(database_path):
    return closing(sqlite3.connect(database_path))

def create_employee(database_path, first_name, last_name):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO employees (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
        connection.commit()
        return cursor.lastrowid

def get_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE id=?", (employee_id,))
        return cursor.fetchone()


def update_employee(database_path, employee_id, name=None, bio=None):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        if name:
            cursor.execute("UPDATE employees SET name=? WHERE id=?", (name, employee_id))
        if bio:
            cursor.execute("UPDATE employees SET bio=? WHERE id=?", (bio, employee_id))
        connection.commit()

def delete_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
        connection.commit()


import sqlite3
from contextlib import closing

def get_connection(database_path):
    return sqlite3.connect(database_path)

def create_employee_table(database_path):
    """Baza sxemaga mos yaratiladi, agar mavjud bo'lmasa"""
    with get_connection(database_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                salary REAL,
                manager_id INTEGER,
                department_id INTEGER
                -- Boshqa ustunlar ham shu yerda bo'ladi (email, phone_number...)
            )
        """)

def create_employee(database_path, first_name, last_name, salary=None):
    with get_connection(database_path) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(
                "INSERT INTO employees (first_name, last_name, salary) VALUES (?, ?, ?)",
                (first_name, last_name, salary)
            )

            return cursor.lastrowid

def get_employee(database_path, employee_id):
    with get_connection(database_path) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("SELECT * FROM employees WHERE id=?", (employee_id,))
            return cursor.fetchone()

def update_employee(database_path, employee_id, first_name=None, last_name=None, salary=None):
    with get_connection(database_path) as conn:
        with closing(conn.cursor()) as cursor:

            if first_name:
                cursor.execute("UPDATE employees SET first_name=? WHERE id=?", (first_name, employee_id))
            if last_name:
                cursor.execute("UPDATE employees SET last_name=? WHERE id=?", (last_name, employee_id))
            if salary is not None:
                cursor.execute("UPDATE employees SET salary=? WHERE id=?", (salary, employee_id))

def delete_employee(database_path, employee_id):
    with get_connection(database_path) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))


db_file = 'hr_database.db'
create_employee_table(db_file)
new_emp_id = create_employee(db_file, "Jalolov", "Doston", 70000,)

print(f"Yangi xodim IDsi: {new_emp_id}")
update_employee(db_file, new_emp_id, salary=65000)
print(f"Yangilangan ma'lumot: {get_employee(db_file, new_emp_id)}")