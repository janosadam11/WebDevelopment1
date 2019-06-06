from smartninja_nosql.odm import Model


class User(Model):
    def __init__(self, name, email, secret_number, password, **kwargs):
        self.name = name
        self.email = email
        self.secret_number = secret_number
        self.password = password

        super().__init__(**kwargs)
