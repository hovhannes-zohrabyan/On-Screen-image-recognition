import pyautogui


def mouse_move_up(distance):
    x, y = pyautogui.position()
    pyautogui.moveTo(None, y - int(distance))


def mouse_move_down(distance):
    x, y = pyautogui.position()
    pyautogui.moveTo(None, y + int(distance))


def mouse_move_left(distance):
    x, y = pyautogui.position()
    pyautogui.moveTo(x - int(distance), None)


def mouse_move_right(distance):
    x, y = pyautogui.position()
    pyautogui.moveTo(x + int(distance), None)


def mouse_click_right():
    pyautogui.click(button='right')


def mouse_click_left():
    pyautogui.click(button='left')
