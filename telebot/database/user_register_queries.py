import os
import psycopg2

def check_user_existance(user_telegram_id:int) -> bool:
    """  
    This function checks existance of a user with user_telegram_id in the database.
    """
    is_user_exists:bool = False
    try:
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        conn.set_isolation_level(0)
        conn.autocommit = True
        cur = conn.cursor()        
    except:
        print("Unable to connect to the database.")        
    if cur:    
        try:
            cur.execute("""
            SELECT user_id
            FROM user_state
            WHERE user_id = %s
            """, (user_telegram_id, ))
            records = cur.fetchall()
            if len(records)>0:
                is_user_exists = True                
        except:
            print("Can\'t to execute check_user_existance query") 
        cur.close()
        conn.close()
    return is_user_exists
    
def set_zero_user_state(user_telegram_id:int) -> bool:
    """  
    This function set user coordinates to zero and monster counter to init value.
    """
    updated_sucessful:bool = False
    try:
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        conn.set_isolation_level(0)
        conn.autocommit = True
        cur = conn.cursor()        
    except:
        print("Unable to connect to the database.")
        
    if cur:    
        try:
            cur.execute("""
            UPDATE user_state 
            SET coordinate_x = DEFAULT, 
            coordinate_y = DEFAULT, 
            time_before_attack = DEFAULT 
            WHERE user_id = %s;
            """, (user_telegram_id, ))
            updated_sucessful = bool(cur.rowcount)            
        except:
            print("Can\'t to execute set_zero_user_state query") 
        cur.close()
        conn.close()
    return updated_sucessful
    
def create_new_user(user_telegram_id:int) -> bool:
    """  
    This function create a new user row and
    set user coordinates to zero and monster counter to default value.
    """
    created_successful:bool = False
    try:
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        conn.set_isolation_level(0)
        conn.autocommit = True
        cur = conn.cursor()        
    except:
        print("Unable to connect to the database.")
        
    if cur:    
        try:
            cur.execute("""
            INSERT INTO user_state (user_id, 
            coordinate_x, 
            coordinate_y, 
            time_before_attack) 
            VALUES (%s, DEFAULT, DEFAULT, DEFAULT)
            """, (user_telegram_id, ))     
            created_successful:bool = True
        except Exception as e:
            print("Can\'t to execute create_new_user query") 
	    print(e)
        cur.close()
        conn.close()
    return created_successful    
    
