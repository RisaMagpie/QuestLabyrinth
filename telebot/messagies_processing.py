from .database import change_user_state

def prepare_answer(msg_text:str, user_id:int) -> (str, list):
    # this dict contains delta coordinates for action if user see from down to up (in y direction)
    # if user see in x direction, this dict need to be inversed
    delta_dict={
        'Пойти прямо': (0, 1),
        'Пойти налево': (-1, 0),
        'Пойти направо': (1, 0),
        'Вернуться назад': (0, -1)
    }
    
    dir_dict={
        # instructions how to change direction
    }
    
    # get user state and get direction
    # direction = ....query
    # need a query!
    
        
    if msg_text in delta_dict:
        #get old direction:
        if direction=='y': # or 0 and 1
            coordinate_x_delta, coordinate_y_delta = delta_dict['msg_text']
        else:
            coordinate_y_delta, coordinate_x_delta = delta_dict['msg_text']
        # change direction
        # change user_state: coordinates, timer, direction(?)
        coordinate_x, coordinate_y = change_user_state.update_state(user_id, 
                                                                    delta_x = coordinate_x_delta, 
                                                                    delta_y = coordinate_y_delta)
        
        #get screenplay part
        # ...answer_text = 
        #get actions
        # ...actions =   
    else:
        answer_text = "Введите, пожалуйста, действие корректно."
        actions = []
    return answer_text, actions