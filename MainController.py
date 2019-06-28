from json import loads, dumps, JSONDecodeError
import json
import os, sys

# User Modules
import MainToolset

# This function is reponsible for parsing and actioning the JSON that we get from server
def action_controller(json):
    # json = {
    #     "images": [
    #         "https://lh5.googleusercontent.com/Hd4hTIRHJWkypd9fqTInph1czas9wBwkfgC1i4RR5M8wpzCBQRjjCoA_Yt8bbzLk1iCAMOKAH2EO7uZXBoRK=w1326-h638",
    #         "https://cdn.shopifycloud.com/hatchful-web/assets/c3a241ae6d1e03513dfed6f5061f4a4b.png",
    #         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8ZzqauwG9epIzOwu7WcHWb3D5DWd_oex3FVGRWcLU0qyLmksY"
    #     ],
    #     "matching_accuracy": "90%",
    #     "app_path": "\/usr\/share\/applications\/app",
    #     "operations": [
    #         {
    #             "type": "mouse",
    #             "direction": "up",
    #             "distance": "100px"
    #         },
    #         {
    #             "type": "mouse",
    #             "direction": "left",
    #             "distance": "200px"
    #         },
    #         {
    #             "type": "mouse",
    #             "click": "left"
    #         },
    #         {
    #             "type": "keyboard",
    #             "do": "command",
    #             "content": "Ctrl + A"
    #         },
    #         {
    #             "type": "keyboard",
    #             "do": "command",
    #             "content": "DELETE"
    #         },
    #         {
    #             "type": "keyboard",
    #             "do": "type",
    #             "content": "QWWERTY"
    #         },
    #         {
    #             "type": "mouse",
    #             "direction": "down",
    #             "distance": "200px"
    #         },
    #         {
    #             "type": "mouse",
    #             "direction": "right",
    #             "distance": "100px"
    #         },
    #         {
    #             "type": "keyboard",
    #             "do": "command",
    #             "content": "Tab"
    #         },
    #         {
    #             "type": "mouse",
    #             "click": "left"
    #         },
    #         {
    #             "type": "keyboard",
    #             "do": "type",
    #             "content": "ZXCVBN"
    #         },
    #         {
    #             "type": "keyboard",
    #             "do": "command",
    #             "content": "Enter"
    #         }
    #     ],
    #     "delay": "2",
    #     "image_search_timeout": "3"
    # }
    # json = {
    #     'error': 'MNA01'
    # }

    if 'error' in json:
        return json['error']
        # sys.exit()

    images_set = json['images']
    accuracy = int(json['matching_accuracy'][:-1])/100
    image_search_timeout = int(json['image_search_timeout'])
    app_path = json['app_path']
    operations_list = json['operations']

    # print(type(accuracy))
    #   Run the Application
    MainToolset.run_application(app_path)

    #   Find Images and start doing the required actions
    MainToolset.find_images_controller(images_set, accuracy, image_search_timeout, operations_list)
