# storefront_data_test = {
#     "banner_enabled": False,
#     "purchase_options": [
#         {
#             "button_text": "Dynamic offer 1 - button_text",
#             "description": "Dynamic offer 1 - description",
#             "id": "",
#             "price": "99.99",
#             "price_text": "price_text",
#             "session_count": "0",
#             "subtitle": "Dynamic offer - subtitle",
#             "title": "Dynamic offer - title",
#             "suffix": "Dynamic offer - suffix",
#             "trial_duration": 0,
#             "min_member_count": 1,
#             "max_member_count": 1,
#             "action": "purchase",
#             "frequency_view": "monthly",
#             "free_learning_subscription": False,
#             "team_type": "personal",
#             "frequency": None,
#             "sth": "something",
#         }
#     ]
# }

from Problem4.problem4.serializable import Serializable


class Storefront(Serializable):
    def __init__(self, storefront_obj={}):
        self.purchase_options = []

        purchase_options = storefront_obj.pop("purchase_options")

        self.__dict__.update(storefront_obj)

        for purchase_option in purchase_options:
            self.purchase_options.append(
                PurchaseOption(purchase_option)
            )


class PurchaseOption(Serializable):
    def __init__(self, purchase_option):
        self.__dict__.update(purchase_option)


# test = Storefront(storefront_data_test)
# print(len(test.purchase_options))


# class Storefront:
#
#     def __init__(self, storefront_obj={}):
#         _storefront_obj = storefront_obj.copy()
#         self.purchase_options = []
#         self.purchase_options = _storefront_obj.pop("purchase_options")
#
#         self.__dict__.update(_storefront_obj)
#
#         for purchase_option in self.purchase_options:
#             self.purchase_options.append(
#                 PurchaseOption(purchase_option)
#             )
#
#
# class PurchaseOption:
#     def __init__(self, purchase_option):
#         self.__dict__.update(purchase_option)
