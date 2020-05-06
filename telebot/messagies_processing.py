from .database.change_user_state import (update_state, get_user_state)
from .database.get_queries import (get_possible_actions_text, get_screenplay_part_text)
from .lists_for_directions_and_actions_processing import (DIRECTIONS, USER_ACTIONS, ACTIONS)


def process_actions_for_direction(possible_actions: list, 
                                  current_direction:str)-> list:
    actions = []
    for possible_action in possible_actions:
        decrement_for_direction_action = DIRECTIONS.index(current_direction)
        action = USER_ACTIONS[(ACTIONS.index(possible_action)-decrement_for_direction_action)%4]
        actions.append(action)
    return actions

def prepare_answer(msg_text:str, user_id:int) -> (str, list):
    # 1. Check can the user go on this direction.
    coordinate_x: int
    coordinate_y: int
    current_direction: str
    time_before_attack: int 
    coordinate_x, coordinate_y, current_direction, time_before_attack = get_user_state(user_id)
    print("User state was got")
    possible_actions: list = get_possible_actions_text(coordinate_x, coordinate_y)
    print("Possible actions were got")
    ## Изменение действия пользователя таким образом, как если бы он смотрел на север.
    ## То есть с точки зрения разработчика, который смотрит на карту.
    print("Current direction: ", current_direction)
    print("User action: ", msg_text)
    increment_for_direction_action = DIRECTIONS.index(current_direction)
    action = ACTIONS[(USER_ACTIONS.index(msg_text)+increment_for_direction_action)%4]
    print("New action: ", action)
    print("Action was changed to north")    

    if action not in possible_actions:
        answer_text = "Это действие выполнить невозможно."
        # Игрок остается в том же состоянии, ему предлагается выполнить действия, которые возможны
        actions = process_actions_for_direction(possible_actions, current_direction)
        print("Return last opportunities")
        return answer_text, actions
    
    # 2. Меняем состояние пользователя.
    ## Меняем координаты.
    delta_dict={
        'Вверх': (0, 1),
        'Налево': (-1, 0),
        'Направо': (1, 0),
        'Вниз': (0, -1)
    }
    delta_x, delta_y = delta_dict[action]
    ## Меняем направление просмотра в зависимости от действия.
    increment_for_direction_action = USER_ACTIONS.index(msg_text)
    print("Current direction:", current_direction)
    direction = DIRECTIONS[(DIRECTIONS.index(current_direction)+increment_for_direction_action)%4]
    print("New direction:", direction)
    coordinate_x_new, coordinate_y_new = update_state(user_id, delta_x, delta_y,
                                                                coordinate_x, coordinate_y, 
                                                                current_direction, time_before_attack,
                                                                direction)
    print("User state was updated")     
    # 3. Вычисляем действия в виде для пользователя.
    # Возвращаем действия и текст сценария.
    actions = get_possible_actions_text(coordinate_x_new, coordinate_y_new)
    answer_text = get_screenplay_part_text(coordinate_x_new, coordinate_y_new)
    print("Actions and screenplay were got") 
    # Перевод действий в координаты пользователя:
    actions = [process_actions_for_direction(actions, direction)]
    print("Actions were changed") 
    return answer_text, actions
