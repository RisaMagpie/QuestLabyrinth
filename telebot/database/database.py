import os
import sys
import psycopg2

"""
Drop all tables of database you given.
"""

DATABASE_URL = os.environ['DATABASE_URL']


def create_database():
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        conn.set_isolation_level(0)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute('''SELECT table_schema,table_name FROM information_schema.tables 
                                WHERE table_schema = 'public' ORDER BY table_schema,table_name;''')
        rows = cur.fetchall()
        for row in rows:
            cur.execute("DROP TABLE IF EXISTS " + row[1] + " cascade")
            print("dropping table: ", row[1])

        cur.execute('''CREATE TABLE  actions_for_state (
            id SERIAL PRIMARY KEY,
            coordinate_x BIGINT NOT NULL CHECK (coordinate_x > 0),
            coordinate_y BIGINT NOT NULL CHECK (coordinate_y > 0),
            possible_action_id integer NOT NULL
        );''')

        cur.execute('''CREATE TABLE actions_id (
            action_id SERIAL PRIMARY KEY,
            action_name character varying(50) NOT NULL
        );''')

        cur.execute('''CREATE TABLE screenplay_for_state (
            id SERIAL PRIMARY KEY,
            coordinate_x BIGINT NOT NULL DEFAULT 0,
            coordinate_y BIGINT NOT NULL,
            current_screenplay_part_id smallint NOT NULL
        );''')

        cur.execute('''CREATE TABLE screenplay_id (
            screenplay_part_id SERIAL PRIMARY KEY,
            screenplay_part_text character varying(50) NOT NULL
        );''')

        cur.execute('''CREATE TABLE user_inventory (
            id SERIAL PRIMARY KEY,
            user_id integer NOT NULL,
            item_name character varying(50) NOT NULL
        );''')

        cur.execute('''CREATE TABLE user_state (
            user_id SERIAL PRIMARY KEY,
            user_name character varying(50) NOT NULL,
            coordinate_x BIGINT NOT NULL CHECK (coordinate_x > 0) UNIQUE,
            coordinate_y BIGINT NOT NULL CHECK (coordinate_y > 0) UNIQUE,
            time_before_attack BIGINT NOT NULL
        );''')

        cur.execute('''ALTER TABLE actions_for_state 
                ADD CONSTRAINT possible_action_id_fk
                FOREIGN KEY (possible_action_id)
                REFERENCES actions_id(action_id) 
                ON UPDATE CASCADE;''')

        cur.execute('''ALTER TABLE screenplay_for_state 
                ADD CONSTRAINT coordinate_x_fk
                FOREIGN KEY (coordinate_x)
                REFERENCES user_state(coordinate_x) 
                ON UPDATE CASCADE;''')

        cur.execute('''ALTER TABLE screenplay_for_state 
                ADD CONSTRAINT coordinate_y_fk
                FOREIGN KEY (coordinate_y)
                REFERENCES user_state(coordinate_y) 
                ON UPDATE CASCADE;''')

        cur.execute('''ALTER TABLE screenplay_for_state 
                ADD CONSTRAINT current_screenplay_part_id_fk
                FOREIGN KEY (current_screenplay_part_id)
                REFERENCES screenplay_id 
                ON UPDATE CASCADE;''')

        cur.execute('''ALTER TABLE user_inventory 
                ADD CONSTRAINT user_id_fk
                FOREIGN KEY (user_id)
                REFERENCES user_state(user_id) 
                ON DELETE CASCADE''')

        print("Table created successfully")
        # con.commit()
        # print("Record inserted successfully")
        print("Operation done successfully")
        cur.close()
        conn.close()
    except:
        print("Unable to connect to the database.")


if __name__ == "__main__":
    create_database()
