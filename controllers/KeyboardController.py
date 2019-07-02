import pyautogui


def keyboard_type(text):
    pyautogui.typewrite(text)


def keyboard_press_single(button):
    button = button.replace(' ', '').lower()
    pyautogui.press(button)


def keyboard_press_combination(button_combination):
    print(button_combination)
    buttons = button_combination.split('+', 1)
    button1 = buttons[0].replace(' ', '').lower()
    button2 = buttons[1].replace(' ', '').lower()

    pyautogui.keyDown(button1)
    pyautogui.press(button2)
    pyautogui.keyUp(button1)
