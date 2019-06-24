import pyautogui


def keyboard_type(text):
    pyautogui.typewrite(text)


def keyboard_press_single(button):
    pyautogui.press('button')


def keyboard_press_combination(button_compbination):
    button_combination = "CTRL + A"
    buttons = button_combination.split('+', 1)
    button1 = buttons[0].replace(' ', '').lower()
    button2 = buttons[1].replace(' ', '').lower()
    print(button1, button2)

    pyautogui.keyDown(button1)
    pyautogui.press(button2)
    pyautogui.keyUp(button1)

keyboard_press_combination("Test")
