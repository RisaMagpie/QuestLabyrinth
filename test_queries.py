from telebot.database import change_user_state as ch
#This function is only for checking work of query functions manually.
def check(user_id:int):
    coordinate_x, coordinate_y, time_before_attack = ch.get_user_state(user_id)
    print(coordinate_x, coordinate_y)
    coordinate_x, coordinate_y = ch.update_state(user_id, delta_x=1, delta_y=-1)
    print(coordinate_x, coordinate_y)