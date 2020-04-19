import os
import sys
import psycopg2

from fill_database import fill_database

"""
Drop all tables of database you given and create whole database.
"""

DATABASE_URL = os.environ['DATABASE_URL']


def create_database():
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        conn.set_isolation_level(0)
        conn.autocommit = True
        cur = conn.cursor()

        print("execute...")
        cur.execute('''SELECT table_schema,table_name FROM information_schema.tables 
                                WHERE table_schema = 'public' ORDER BY table_schema,table_name;''')
        rows = cur.fetchall()

        print("dropping existed tables")
        for row in rows:
            cur.execute("DROP TABLE IF EXISTS " + row[1] + " cascade")
            print("dropping table: ", row[1])

        print("creating tables...")

        cur.execute('''CREATE TABLE actions_id (
            action_id SERIAL PRIMARY KEY,
            action_name character varying(50) NOT NULL,
            UNIQUE (action_name)
        );''')
        print("actions_id table created 1/6")

        cur.execute('''CREATE TABLE screenplay_for_state (
            coordinate_x BIGINT NOT NULL,
            coordinate_y BIGINT NOT NULL,
            current_screenplay_part_id smallint NOT NULL,
            PRIMARY KEY(coordinate_x, coordinate_y)
        );''')  # screenplay 1:m coordinates, actions m:m
        print("screenplay_for_state table created 2/6")

        cur.execute('''CREATE TABLE actions_for_state (
            id SERIAL PRIMARY KEY,
            coordinate_x BIGINT NOT NULL,
            coordinate_y BIGINT NOT NULL,
            possible_action_id integer NOT NULL,
            UNIQUE(coordinate_x, coordinate_y, possible_action_id)            
        );''')  # screenplay 1:m coordinates, actions m:m
        print("actions_for_state table created 3/6")

        cur.execute('''CREATE TABLE screenplay_id (
            screenplay_part_id SERIAL PRIMARY KEY,
            screenplay_part_text character varying(50) NOT NULL,
            UNIQUE (screenplay_part_text)
        );''')
        print("screenplay_id table created 4/6")

        cur.execute('''CREATE TABLE user_inventory (
            id SERIAL PRIMARY KEY,
            user_id integer NOT NULL,
            item_name character varying(50) NOT NULL,
            UNIQUE(user_id, item_name)
        );''')
        print("user_inventory table created 5/6")

        cur.execute('''CREATE TABLE user_state (
            user_id BIGINT PRIMARY KEY,
            coordinate_x BIGINT NOT NULL DEFAULT 0,
            coordinate_y BIGINT NOT NULL DEFAULT 0,
            time_before_attack BIGINT NOT NULL DEFAULT 1000
        );''')
        print("user_state table created 6/6")

        cur.execute('''ALTER TABLE actions_for_state 
                    ADD CONSTRAINT possible_action_id_fk
                    FOREIGN KEY (possible_action_id)
                    REFERENCES actions_id(action_id) 
                    ON DELETE CASCADE ON UPDATE CASCADE;''')
        print("possible_action_id_fk created 1/5")

        cur.execute('''ALTER TABLE actions_for_state 
                    ADD CONSTRAINT action_coordinates_id_fk
                    FOREIGN KEY (coordinate_x,coordinate_y)
                    REFERENCES screenplay_for_state(coordinate_x,coordinate_y) 
                    ON DELETE CASCADE ON UPDATE CASCADE;''')
        print("action_coordinates_id_fk created 2/5")

        cur.execute('''ALTER TABLE user_state 
                    ADD CONSTRAINT user_coordinates_fk
                    FOREIGN KEY (coordinate_x,coordinate_y)
                    REFERENCES screenplay_for_state(coordinate_x,coordinate_y) 
                    ON DELETE CASCADE ON UPDATE CASCADE;''')
        print("user_coordinates_fk created 3/5")

        cur.execute('''ALTER TABLE screenplay_for_state 
                    ADD CONSTRAINT current_screenplay_part_id_fk
                    FOREIGN KEY (current_screenplay_part_id)
                    REFERENCES screenplay_id(screenplay_part_id)
                    ON DELETE CASCADE ON UPDATE CASCADE;''')
        print("current_screenplay_part_id_fk created 4/5")

        cur.execute('''ALTER TABLE user_inventory 
                    ADD CONSTRAINT user_id_fk
                    FOREIGN KEY (user_id)
                    REFERENCES user_state(user_id) 
                    ON DELETE CASCADE ON UPDATE CASCADE;''')
        print("user_id_fk created 5/5")

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
    fill_database()
