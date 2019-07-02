import pyautogui
pyautogui.FAILSAFE = False

import controllers.MouseController
import controllers.KeyboardController


def make_action(action_json):
    type_of_operation = action_json['type']
    speciality_of_operation = 'mouse_move'

    if type_of_operation == 'mouse':
        if 'direction' in action_json and 'distance_of_json':
            speciality_of_operation = 'mouse_move_' + action_json['direction']
            print(speciality_of_operation)
        if 'click' in action_json:
            # click_of_operation =  action_json['click']
            speciality_of_operation = 'mouse_click_' + action_json['click']
            print(speciality_of_operation)
    elif type_of_operation == 'keyboard':
        if action_json['do'] == 'command':
            speciality_of_operation = 'keyboard_press'
            print(speciality_of_operation)
        if action_json['do'] == 'type':
            speciality_of_operation = 'keyboard_type'
            print(speciality_of_operation)

    autogui_controller(speciality_of_operation, action_json)


def autogui_controller(speciality_of_operation, action_data):

    speciality_of_operation = speciality_of_operation.split('_')

    if speciality_of_operation[0] == 'mouse':
        if speciality_of_operation[1] == 'move':
            distance = action_data['distance'][:2]
            direction = speciality_of_operation[2]
            if direction == 'down':
                controllers.MouseController.mouse_move_down(distance)
            if direction == 'up':
                controllers.MouseController.mouse_move_up(distance)
            if direction == 'left':
                controllers.MouseController.mouse_move_left(distance)
            if direction == 'right':
                controllers.MouseController.mouse_move_right(distance)
        if speciality_of_operation[1] == 'click':
            button = speciality_of_operation[2]
            if button == 'left':
                controllers.MouseController.mouse_click_left()
            if button == 'right':
                controllers.MouseController.mouse_click_right()

    elif speciality_of_operation[0] == 'keyboard':
        if speciality_of_operation[1] == 'type':
            controllers.KeyboardController.keyboard_type(action_data['content'])
        if speciality_of_operation[1] == 'press':
            print(len(action_data['content'].split('+')))
            if len(action_data['content'].split('+')) > 1:
                controllers.KeyboardController.keyboard_press_combination(action_data['content'])
            else:
                controllers.KeyboardController.keyboard_press_single(action_data['content'])


