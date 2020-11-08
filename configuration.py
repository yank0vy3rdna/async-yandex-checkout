class Configuration:
    shop_id = None

    secret_key = None

    def configure(self, shop_id, secret_key):
        self.shop_id = shop_id
        self.secret_key = secret_key


configuration = Configuration()
