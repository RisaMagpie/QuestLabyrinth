
# coding: utf-8

# In[ ]:


import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

def get_possible_actions_text(coordinate_x:int,coordinate_y:int)->[str]:
    """Get possible actions by coordinates."""
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        conn.set_isolation_level(0)
        conn.autocommit = True
        cur = conn.cursor()        
    except:
        print("Unable to connect to the database.")   
    if cur:    
        try:
            cur.execute("""
            SELECT action_name 
            FROM actions_id 
            INNER JOIN actions_for_state 
            ON action_id = possible_action_id 
            WHERE coordinate_x= %s AND coordinate_y= %s;
            """, (coordinate_x,coordinate_y))
            result = [item[0] for item in cur.fetchall()]

        except:
            print("Can\'t to execute get_user_state query") 
        cur.close()
        conn.close()
    return result

if __name__ == "__main__":
    print(get_possible_actions_text(0,0))

