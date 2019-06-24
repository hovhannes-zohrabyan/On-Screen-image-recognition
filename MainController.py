from json import loads, dumps, JSONDecodeError
import json
import os, sys

# User Modules
import MainToolset


# This function is reponsible for parsing and actioning the JSON that we get from server
def action_controller(json):
    json = {
        "images": [
            "https://about.canva.com/wp-content/uploads/sites/3/2016/08/Band-Logo.png",
            "https://cdn.shopifycloud.com/hatchful-web/assets/c3a241ae6d1e03513dfed6f5061f4a4b.png",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8ZzqauwG9epIzOwu7WcHWb3D5DWd_oex3FVGRWcLU0qyLmksY"
        ],
        "matching_accuracy": "90%",
        "app_path": "\/usr\/share\/applications\/app",
        "operations": [
            {
                "type": "mouse",
                "direction": "up",
                "distance": "100px"
            },
            {
                "type": "mouse",
                "direction": "left",
                "distance": "200px"
            },
            {
                "type": "mouse",
                "click": "left"
            },
            {
                "type": "keyboard",
                "do": "command",
                "content": "Ctrl + A"
            },
            {
                "type": "keyboard",
                "do": "command",
                "content": "DELETE"
            },
            {
                "type": "keyboard",
                "do": "type",
                "content": "QWWERTY"
            },
            {
                "type": "mouse",
                "direction": "down",
                "distance": "200px"
            },
            {
                "type": "mouse",
                "direction": "right",
                "distance": "100px"
            },
            {
                "type": "keyboard",
                "do": "command",
                "content": "Tab"
            },
            {
                "type": "mouse",
                "click": "left"
            },
            {
                "type": "keyboard",
                "do": "type",
                "content": "ZXCVBN"
            },
            {
                "type": "keyboard",
                "do": "command",
                "content": "Enter"
            }
        ],
        "delay": "2",
        "image_search_timeout": "30"
    }
    # json = {
    #     'error': 'MNA01'
    # }

    if 'error' in json:
        print(json['error'])
        sys.exit()

    images_set = json['images']
    accuracy = int(json['matching_accuracy'][:-1])/100
    app_path = json['app_path']
    operations_list = json['operations']

    # print(type(accuracy))
    #   Run the Application
    MainToolset.run_application(app_path)

    #   Find Images and start doing the required actions
    MainToolset.find_images_controller(images_set, accuracy, operations_list)
