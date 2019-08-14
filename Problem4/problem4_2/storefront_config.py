"""
xu li purchase options:
bang cach loc qua tung gia tri trong list thanh 1 dict rieng
"""


class PurchaseOption:
    def __init__(self, my_purchase_dict):
        self.button_text = my_purchase_dict.get('button_text')
        self.description = my_purchase_dict.get('description')
        self.id = my_purchase_dict.get('id')
        self.price = my_purchase_dict.get('price')
        self.price_text = my_purchase_dict.get('price_text')
        self.session_count = my_purchase_dict.get('session_count')
        self.subtitle = my_purchase_dict.get('subtitle')
        self.title = my_purchase_dict.get('title')
        self.suffix = my_purchase_dict.get('suffix')
        self.trial_duration = my_purchase_dict.get('trial_duration')
        self.min_member_count = my_purchase_dict.get('min_member_count')
        self.max_member_count = my_purchase_dict.get('max_member_count')
        self.action = my_purchase_dict.get('action')
        self.frequency_view = my_purchase_dict.get('frequency_view')
        self.free_learning_subscription = my_purchase_dict.get('free_learning_subscription')
        self.team_type = my_purchase_dict.get('team_type')
        self.frequency = my_purchase_dict.get('frequency')

    def update_purchase(self, purchase_data):
        self.button_text = purchase_data.get('button_text', self.button_text)
        self.description = purchase_data.get('description', self.description)
        self.id = purchase_data.get('id', self.id)
        self.price = purchase_data.get('price', self.price)
        self.price_text = purchase_data.get('price_text', self.price_text)
        self.session_count = purchase_data.get('session_count', self.session_count)
        self.subtitle = purchase_data.get('subtitle', self.subtitle)
        self.title = purchase_data.get('title', self.title)
        self.suffix = purchase_data.get('suffix', self.suffix)
        self.trial_duration = purchase_data.get('trial_duration', self.trial_duration)
        self.min_member_count = purchase_data.get('min_member_count', self.min_member_count)
        self.max_member_count = purchase_data.get('max_member_count', self.max_member_count)
        self.action = purchase_data.get('action', self.action)
        self.frequency_view = purchase_data.get('frequency_view', self.frequency_view)
        self.free_learning_subscription = purchase_data.get('free_learning_subscription', self.free_learning_subscription)
        self.team_type = purchase_data.get('team_type', self.team_type)
        self.frequency = purchase_data.get('frequency', self.frequency)

    def to_dict(self):
        return self.__dict__


class Storefront:
    def __init__(self, storefront_dict):
        self.banner_enabled = storefront_dict.get('banner_enabled')
        self.banner_text = storefront_dict.get('banner_text')
        self.banner_enabled = storefront_dict.get('banner_enabled')
        self.description = storefront_dict.get('description')
        self.enabled = storefront_dict.get('enabled')

        purchase_options = storefront_dict['purchase_options']
        for index, value in enumerate(purchase_options):
            purchase_options[index] = PurchaseOption(value)
        self.purchase_options = purchase_options

    def update_storefront(self, storefront_data):
        self.banner_enabled = storefront_data.get('banner_enabled', self.banner_enabled)
        self.banner_text = storefront_data.get('banner_text', self.banner_text)
        self.banner_enabled = storefront_data.get('banner_enabled', self.banner_enabled)
        self.description = storefront_data.get('description', self.description)
        self.enabled = storefront_data.get('enabled', self.enabled)

        for index, value in enumerate(storefront_data['purchase_options']):
            self.purchase_options[index].update_purchase(value)

    def to_dict(self):
        storefront_data = self.__dict__.copy()
        options = storefront_data['purchase_options']
        for key, value in enumerate(options):
            options[key] = value.to_dict()
        return storefront_data


class StorefrontConfig:
    def __init__(self, storefront_config_dict):
        self.expiration_time = storefront_config_dict.get('expiration_time')
        self.id = storefront_config_dict.get('id')
        self.product = storefront_config_dict.get('product')
        self.storefront = Storefront(storefront_config_dict.get('storefront'))
        self.utm_campaign = storefront_config_dict.get('utm_campaign')
        self.utm_source = storefront_config_dict.get('utm_source')

    def update_storefront_config(self, storefront_config_data):
        self.expiration_time = storefront_config_data.get('expiration_time', self.expiration_time)
        self.id = storefront_config_data.get('id', self.id)
        self.product = storefront_config_data.get('product', self.product)
        self.storefront.update_storefront(storefront_config_data.get('storefront', self.storefront))
        self.utm_campaign = storefront_config_data.get('utm_campaign', self.utm_campaign)
        self.utm_source = storefront_config_data.get('utm_source', self.utm_source)

    def to_dict(self):
        storefront_config = self.__dict__.copy()
        storefront_config['storefront'] = storefront_config['storefront'].to_dict()
        return storefront_config
