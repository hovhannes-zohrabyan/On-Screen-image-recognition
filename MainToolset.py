import os
import requests

import OperationController
from image_search_module.imagesearch import *

# TODO: Test on Ubuntu Based System
def run_application(app_path):
    os.system('bash -c ' + app_path)


def find_images_controller(images_set, accuracy, image_search_timeout,  operations_list):
    print(images_set)

    i = 0
    for img in images_set:
        image_name = 'temp_images/' + str(i) + '.png'
        f = open(image_name, 'wb')
        f.write(requests.get(img).content)
        f.close()
        response = find_image(image_name, accuracy, image_search_timeout)
        if response == 'Not Found':
            pass
        else:
            make_actions(operations_list)
        i += 1


#TODO: Move to another controller
def find_image(image_name, accuracy, image_search_timeout):
    pos = imagesearch_loop(image_name, 0.1, accuracy, image_search_timeout)
    if pos == "Not Found":
        return 'Not Found'
    pyautogui.moveTo(pos[0], pos[1])
    print("image found ", pos[0], pos[1])


# TODO: Rename
def make_actions(operations_list):
    for operation in operations_list:
        OperationController.make_action(operation)
