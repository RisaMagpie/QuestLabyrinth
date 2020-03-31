
# coding: utf-8


import psycopg2
import sys

"""
Drop all tables of database you given.
"""

try:
    conn = psycopg2.connect("dbname='quest_labyrinth2' user='postgres' password='5114938w'")
    conn.set_isolation_level(0)
    conn.autocommit = True 
except:
    print("Unable to connect to the database."
)
cur = conn.cursor()

try:
    cur.execute("SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema,table_name")
    rows = cur.fetchall()
    for row in rows:
        print("dropping table: ", row[1])
        cur.execute("drop table " + row[1] + " cascade")
#     cur.close()
#     conn.close()
except:
    print ("Error: ", sys.exc_info()[1])


# In[34]:


#cur.execute('''CREATE DATABASE "quest_labyrinth2" WITH ENCODING = 'UTF8';''') 
#TO DO: look into how to drop whole database and create new, no kust clean it

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
con.close()

