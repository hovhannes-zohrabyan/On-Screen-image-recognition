import pyautogui


def make_action(action_json):
    type_of_operation = action_json['type']
    speciality_of_operation = 'mouse_move'

    if type_of_operation == 'mouse':
        if 'direction' in action_json:
            direction_of_operation = action_json['direction']
        if 'distance' in action_json:
            distance_of_operation = action_json['distance']
        if 'click' in action_json:
            click_of_operation =  action_json['click']
            speciality_of_operation = 'mouse_click'
    elif type_of_operation == 'keyboard':
        do_of_operation = action_json['do']
        content_of_operation = action_json['content']
        speciality_of_operation = 'keyboard_click'