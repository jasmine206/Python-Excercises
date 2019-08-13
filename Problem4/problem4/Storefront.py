class Storefront:
    purchase_options = []

    def __init__(self, storefront_obj={}):
        _storefront_obj = storefront_obj.copy()

        purchase_options = _storefront_obj.pop("purchase_options")

        self.__dict__.update(_storefront_obj)

        for purchase_option in purchase_options:
            self.purchase_options.append(
                PurchaseOption(purchase_option)
            )


class PurchaseOption:
    def __init__(self, purchase_option):
        self.__dict__.update(purchase_option)
