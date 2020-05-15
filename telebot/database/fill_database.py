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
        (1, 'Вот оно, начало Вашего опасного пути'),
        (2, 'Вы идете по коридору освещенному факелами'),
        (3, 'Вы были убиты монстром, Ваш склет останется в лабиринте навечно'),
        (4, 'Торжествуйте! Вам удалось выбраться из лабиринта.'),
        (5, 'К сожалению, вы зашли в тупик, из-за стены доносится странный скрежет и свист'),
        (6, 'Тьма сгущается'),
        (7, 'Лабиринт делает резкий поворот'),
        (8, 'Зловонное дыхание преследует Вас'),
        (9, 'Остаётся лишь призрачный шанс на спасение'),
        (10, 'Под ногами у Вас разверзается бездна'),
        (11, 'Время истекает, скорее ищите выход'),
        (12, 'Странный холод окутывает всё вокруг'),
        (13, 'От страха кровь стынет в жилах'),
        (14, 'Леденящий душу крик раздаётся в сумраке'),
        (15, 'Вы чувствуте на себе чей-то взгляд'),
        (16, 'Стены начинают давить на Вас'),
        (17, 'Ужасающий образ мелькнул в углу'),
        (18, 'Вы постоянно чувствуте чьё-то присутствие'),
        (19, 'Вы явно не один'),
        (20, 'Смерть ожидает Вас за каждым углом'),
        (21, 'Ждать помощь бесполезно')
                     
    )

    actions_for_state_data = ([
        (0, 0, 2),
        (0, 0, 3),
        (1, 0, 2),
        (1, 0, 4),
        (-1, 0, 2),
        (-1, 0, 3),
        (-1, 0, 4),
        (2, 0, 1),
        (2, 0, 4),
        (-2, 0, 3),
        (-2, 0, 4),

        (0, 1, 1),
        (0, 1, 3),
        (-1, 1, 1),
        (-1, 1, 2),
        (1, 1, 1),
        (1, 1, 2),
        (1, 1, 3),
        (2, 1, 4),
        (2, 1, 2),
        (-2, 1, 1),
        (-2, 1, 3),

        (0, -1, 2),
        (-1, -1, 1),
        (-1, -1, 2),
        (-1, -1, 3),
        (-1, -1, 4),
        (1, -1, 1),
        (1, -1, 3),
        (2, -1, 1),
        (2, -1, 2),
        (2, -1, 4),
        (-2, -1, 1),
        (-2, -1, 3),

        (0, 2, 2),
        (0, 2, 3),
        (0, 2, 4),
        (-1, 2, 2),
        (-1, 2, 3),
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
        (-1, -2, 1),
        (-1, -2, 2),
        (-1, -2, 3),
        (1, -2, 2),
        (1, -2, 3),
        (2, -2, 1),
        (2, -2, 2),
        (-2, -2, 3),

    ]
    )

    screenplay_for_state_data = (
        (0, 0, 1),
        (-2, 3, 4),
        (1, 0, 2),
        (2, 0, 6),
        (-1, 0, 7),
        (-2, 0, 8),

        (0, 1, 9),
        (-1, 1, 12),
        (1, 1, 11),
        (2, 1, 10),
        (-2, 1, 15),

        (0, -1, 5),
        (-1, -1, 13),
        (1, -1, 14),
        (2, -1, 17),
        (-2, -1, 18),

        (0, 2, 7),
        (-1, 2, 13),
        (1, 2, 12),
        (2, 2, 19),
        (-2, 2, 20),

        (0, -2, 21),
        (-1, -2, 8),
        (1, -2, 11),
        (2, -2, 16),
        (-2, -2, 5),

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
