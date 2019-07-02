import os
import requests
from subprocess import *
import time


import OperationController
from image_search_module.imagesearch import *


# TODO: Test on Ubuntu Based System
def run_application(app_path):
    c = app_path

    handle = Popen(c, shell=True)
    time.sleep(5)
    # print
    # handle.stdout.read()
    # handle.flush()


def find_images_controller(images_set, accuracy, image_search_timeout, operations_list, delay):
    print(images_set)

    if not os.path.exists('/usr/bin/root/temp_images'):
        os.makedirs('/usr/bin/root/temp_images')

    i = 0
    for img in images_set:
        image_name = '/usr/bin/root/temp_images/' + str(i) + '.png'
        f = open(image_name, 'wb')
        f.write(requests.get(img).content)
        f.close()
        response = find_image(image_name, accuracy, image_search_timeout)
        if response == 'Not Found':
            pass
        else:
            make_actions(operations_list, delay)
        i += 1


#TODO: Move to another controller
def find_image(image_name, accuracy, image_search_timeout):
    pos = imagesearch_loop(image_name, 0.1, accuracy, image_search_timeout)
    if pos == "Not Found":
        return 'Not Found'
    pyautogui.moveTo(pos[0], pos[1])
    print("image found ", pos[0], pos[1])


# TODO: Rename
def make_actions(operations_list, delay):
    for operation in operations_list:
        OperationController.make_action(operation)
        time.sleep(delay)

