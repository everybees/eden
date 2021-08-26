class Merchant():
    business_reg = "RC34524"


    def __init__(self, username, store_name, first_name, last_name, email, password):
        self.store_name = store_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.username = username


    def log_in(self, username, password):
        if username is self.username and password is self.password:
            return "welcomed back"
        else:
            return "check ur email and password are correct"

