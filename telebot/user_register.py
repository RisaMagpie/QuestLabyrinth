from .database import user_register_queries


def registration(user_telegram_id:int) -> (bool, str, list):
    """
    Before creation of a new user we need to check his existance in the database.
    If user exists we need to update his state to init state.
    Otherwise we need to create a new user with init state in a user_state table.
    After that we need to return from database text message and possible actions.
    """
    is_exist:bool = user_register_queries.check_user_existance(user_telegram_id)
    
    if is_exist:
        is_created:bool = user_register_queries.set_zero_user_state(user_telegram_id)
    else:
        is_created:bool = user_register_queries.create_new_user(user_telegram_id)
            
    # !!!        
    # After that we need to return from database text message and possible actions.
    # But now database is empty.
    # For example:
    text:str = "Вы очнулись в точке (0, 0), позади вас и справа от вас есть проход."
    actions:list = [["пойти назад", "пойти направо"]]
    actions.append(["начать сначала"])
 
    return is_created, text, actions
    
