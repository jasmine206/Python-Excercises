import json
import time

modify_data = {
    "expiration_time": 200,
    "product": "qchat",
    "utm_campaign": str(time.time()),
    "storefront": {
        "banner_enabled": False,
        "purchase_options": [
            {
                "button_text": "Dynamic offer 1 - button_text",
                "description": "Dynamic offer 1 - description",
                "id": "",
                "price": "99.99",
                "price_text": "price_text",
                "session_count": "0",
                "subtitle": "Dynamic offer - subtitle",
                "title": "Dynamic offer - title",
                "suffix": "Dynamic offer - suffix",
                "trial_duration": 0,
                "min_member_count": 1,
                "max_member_count": 1,
                "action": "purchase",
                "frequency_view": "monthly",
                "free_learning_subscription": False,
                "team_type": "personal",
                "frequency": None,
                "sth": "something",
            }
        ]
    }
}


class StorefrontConfig:
    def __init__(self, _object):
        self.object = _object

    def update(self, json_dict):
        for item in json_dict:
            if item in modify_data:
                json_dict[item] = modify_data.get(item)
        return StorefrontConfig(json_dict)


class FileController:
    def read_file(self, readfile):
        with open(readfile, 'r') as f:
            json_to_python = json.load(f)
        return json_to_python

    def write_file(self, dict_object, json_file_name):
        with open(json_file_name, 'w') as json_file:
            json.dump(dict_object, json_file)


# read json file
file_controller = FileController()
config = file_controller.read_file("data.json")

# update values in a dict
storefrontConfig = StorefrontConfig()
updated_dict = storefrontConfig.update(config)

# write into a json file
file_controller.write_file(config, 'result.json')
