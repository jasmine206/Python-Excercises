import json
import time
from Problem4.problem4_2.storefront_config import StorefrontConfig


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
    },
    "additional1": 1,
    "additional2": "something"
}

class FileController:
    def read_file(self, readfile):
        with open(readfile, 'r') as f:
            json_to_python = json.load(f)
        return StorefrontConfig(json_to_python)

    def write_file(self, storefront_config, json_file_name):
        with open(json_file_name, 'w') as json_file:
            json.dump(storefront_config.to_dict(), json_file)


# read json file
file_controller = FileController()
config = file_controller.read_file("data2.json")

# update
config.update(modify_data)
# print(config.storefront.purchase_options[0].button_text)

# write into a json file
file_controller.write_file(config, 'result.json')

