import psycopg2

"""
Fill database.
"""

DATABASE_URL = os.environ['DATABASE_URL']

actions_names = (
    (1, 'Пойти прямо'),
    (2, 'Пойти налево'),
    (3, 'Пойти направо'),
    (4, 'Вернуться назад')
)


def fill_database():
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        conn.set_isolation_level(0)
        conn.autocommit = True
        cur = conn.cursor()
        query = "INSERT INTO actions_id (action_id,action_name) VALUES (%s,%s)"
        cur.executemany(query, actions_names)
        print('Filled actions_id table')
    except:
        print("Unable to connect to the database.")
