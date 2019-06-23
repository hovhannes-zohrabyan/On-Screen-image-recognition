import os
import requests
from image_search_module.imagesearch import *


# TODO: Test on Ubuntu Based System
def run_application(app_path):
    want_run = 'ls'
    os.system('bash -c ' + want_run)


def find_images_controller(images_set, accuracy):
    print(images_set)

    i = 0
    for img in images_set:
        image_name = 'temp_images/' + str(i) + '.png'
        f = open(image_name, 'wb')
        f.write(requests.get(img).content)
        f.close()
        find_image(image_name, accuracy)
        i += 1


#TODO: Move to another controller
def find_image(image_name, accuracy):
    pos = imagesearch_loop(image_name, accuracy)
    pyautogui.moveTo(pos[0], pos[1])
    print("image found ", pos[0], pos[1])

# TODO: Rename
# def make_actions()
