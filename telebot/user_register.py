from .database import user_register_queries
from .database import get_queries as get
from .messagies_processing import process_actions_for_direction

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
            
    actions = []      
    if is_created:
        text = get.get_screenplay_part_text(0, 0)
        actions.append(get.get_possible_actions_text(0, 0))
        actions = process_actions_for_direction(actions, 'north')
    else:
        text = "Извините, что-то пошло не так и Вы не были зарегистрированы"

    return is_created, text, actions
    
