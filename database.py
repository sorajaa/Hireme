import sqlite3

def init_db():
    conn = sqlite3.connect('db/hireme.db')
    cursor = conn.cursor()

    # Makse sure to paste your sql create query of students inside the literals('''''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
    usn TEXT PRIMARY KEY NOT NULL,
    student_name TEXT NOT NULL,
    contact_number TEXT NOT NULL,
    college_name TEXT NOT NULL,
    branch TEXT NOT NULL,
    skills TEXT,
    email_id TEXT NOT NULL,
    password TEXT NOT NULL
);
    ''')
    # Makse sure to paste your sql create query of recruiters inside the literals('''''')
    cursor.execute('''

    ''')

    # Makse sure to paste your sql create query of jobs inside the literals('''''')

    cursor.execute('''


    ''')

    # Makse sure to paste your sql create query of student_applications inside the literals('''''')

    cursor.execute('''

    ''')

    conn.commit()
    conn.close()
