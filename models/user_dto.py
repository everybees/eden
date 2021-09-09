from models.customer import Customer


class User_Dto(Customer):

    def __init__(self, first_name, last_name, password, email, user_name):
        super(User_Dto, self).__init__(first_name=first_name, last_name=last_name,
                                       password=password, email=email, user_name=user_name)