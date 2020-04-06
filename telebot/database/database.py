import os
import sys
import psycopg2
#from credentials import db_name,user,password

"""
Drop all tables of database you given.
"""

DATABASE_URL = os.environ['DATABASE_URL']

def database():
    try:
        #conn = psycopg2.connect(dbname=db_name, user=user, password=password)
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
            coordinate_x BIGINT NOT NULL,
            coordinate_y BIGINT NOT NULL,
            possible_action_id integer NOT NULL
            );''')
        cur.execute('''CREATE TABLE actions_id (
            action_id SERIAL PRIMARY KEY,
            action_name character varying(50) NOT NULL
            );''')
        cur.execute('''CREATE TABLE screenplay_for_state (
            id SERIAL PRIMARY KEY,
            coordinate_x BIGINT NOT NULL,
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
            coordinate_x BIGINT NOT NULL,
            coordinate_y BIGINT NOT NULL,
            time_before_attack BIGINT NOT NULL
            );''')
        print("Table created successfully")
        # con.commit()
        # print("Record inserted successfully")
        print("Operation done successfully")
        conn.close()
    except:
        print("Unable to connect to the database.")


if __name__ == "__main__":
    database()
    
