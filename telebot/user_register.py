from database import user_register_queries

def registration(user_telegram_id:int):
    """
    Before creation of a new user we need to check his existance in the database.
    If user exists we need to update his state to zero-state.
    If user doesn't exist we need to create a new user with zero-state in a user_state.
    After that we need to return from database text message and possible actions.
    """
    is_exist:bool = user_register_queries.check_user_existance(user_telegram_id)
        
    if is_exist:
        is_created:bool = user_register_queries.set_zero_user_state(user_telegram_id)
    else:
        is_created:bool = user_register_queries.add_new_user(user_telegram_id)
 
    return is_created
    