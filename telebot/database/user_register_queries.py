import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

def check_user_existance(user_telegram_id:int):
    """  
    This function checks existance of a user with user_telegram_id in the database.
    """
    return :bool
    
def set_zero_user_state(user_telegram_id:int):
    """  
    This function set user coordinates to zero and monster counter to default value.
    """
    return :bool
    
def add_new_user(user_telegram_id:int):
    """  
    This function create a new user row and
    set user coordinates to zero and monster counter to default value.
    """
    return :bool

    
    