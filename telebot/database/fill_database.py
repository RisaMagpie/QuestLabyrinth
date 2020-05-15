import os

import psycopg2

"""
Fill database.
"""

DATABASE_URL = os.environ['DATABASE_URL']


def fill_database():
    actions_id_data = (
        (1, 'Вверх'),
        (2, 'Налево'),
        (3, 'Направо'),
        (4, 'Вниз')
    )

    screenplay_id_data = (
        (1, 'Вы в начале пути'),
        (2, 'Вы переместились в новую точку'),
        (3, 'Вы были убиты монстром'),
        (4, 'Вы победили')
    )

    actions_for_state_data = ([
        (0, 0, 3),
        (0, 0, 2),
        (1, 0, 4),
        (1, 0, 2),
        (-1, 0, 3),
        (-1, 0, 2),
        (-1, 0, 4),
        (2, 0, 1),
        (2, 0, 4),
        (-2, 0, 3),
        (-2, 0, 4),

        (0, 1, 1),
        (0, 1, 3),
        (-1, 1, 2),
        (-1, 1, 1),
        (1, 1, 3),
        (1, 1, 2),
        (1, 1, 1),
        (2, 1, 4),
        (2, 1, 2),
        (-2, 1, 3),
        (-2, 1, 1),

        (0, -1, 2),
        (-1, -1, 1),
        (-1, -1, 3),
        (-1, -1, 2),
        (-1, -1, 4),
        (1, -1, 1),
        (1, -1, 3),
        (2, -1, 1),
        (2, -1, 4),
        (2, -1, 2),
        (-2, -1, 3),
        (-2, -1, 1),

        (0, 2, 2),
        (0, 2, 3),
        (0, 2, 4),
        (-1, 2, 3),
        (-1, 2, 2),
        (-1, 2, 4),
        (1, 2, 2),
        (1, 2, 3),
        (1, 2, 4),
        (2, 2, 2),
        (-2, 2, 1),
        (-2, 2, 3),
        (-2, 2, 4),

        (0, -2, 2),
        (0, -2, 3),
        (-1, -2, 2),
        (-1, -2, 3),
        (-1, -2, 1),
        (1, -2, 2),
        (1, -2, 3),
        (2, -2, 2),
        (2, -2, 1),
        (-2, -2, 3),

    ]
    )

    screenplay_for_state_data = (
        (0, 0, 1),
        (-2, 3, 4),
        (1, 0, 2),
        (2, 0, 2),
        (-1, 0, 2),
        (-2, 0, 2),

        (0, 1, 2),
        (-1, 1, 2),
        (1, 1, 2),
        (2, 1, 2),
        (-2, 1, 2),

        (0, -1, 2),
        (-1, -1, 2),
        (1, -1, 2),
        (2, -1, 2),
        (-2, -1, 2),

        (0, 2, 2),
        (-1, 2, 2),
        (1, 2, 2),
        (2, 2, 2),
        (-2, 2, 2),

        (0, -2, 2),
        (-1, -2, 2),
        (1, -2, 2),
        (2, -2, 2),
        (-2, -2, 2),

        (-1000, -1000, 3),
    )
    
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        conn.set_isolation_level(0)
        conn.autocommit = True
        cur = conn.cursor()

        query = "INSERT INTO actions_id (action_id,action_name) VALUES (%s,%s)"
        cur.executemany(query, actions_id_data)
        print('Filled actions_id table')

        query = "INSERT INTO screenplay_id (screenplay_part_id,screenplay_part_text) VALUES (%s,%s)"
        cur.executemany(query, screenplay_id_data)
        print('Filled screenplay_id table')

        query = "INSERT INTO screenplay_for_state (coordinate_x,coordinate_y,current_screenplay_part_id) " \
                "VALUES (%s,%s,%s)"
        cur.executemany(query, screenplay_for_state_data)
        print('Filled screenplay_for_state table')
        
        query = "INSERT INTO actions_for_state (id,coordinate_x,coordinate_y,possible_action_id) " \
                "VALUES (DEFAULT,%s,%s,%s)"
        cur.executemany(query, actions_for_state_data)
        print('Filled actions_for_state table')

        print("Operation done successfully")
        cur.close()
        conn.close()
    except:
        print("Unable to connect to the database.")
