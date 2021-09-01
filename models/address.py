class Address:
    def __init__(self, house_number: int = 0, street_name: str = "", city_name: str = "", state_name: str = "",
                 country_name: str = "", ):
        self.__house_number: int = house_number
        self.__street_name: str = street_name
        self.__city_name: str = city_name
        self.__state_name: str = state_name
        self.__country_name: str = country_name

    @property
    def get__house_number(self):
        return self.__house_number

    def update__house_number(self, new_house_number: str):
        self.__house_number = new_house_number

    @property
    def get__street_name(self):
        return self.__street_name

    def update_street_name(self, new_street_name):
        self.__street_name = new_street_name

    @property
    def get__city_name(self):
        return self.__city_name

    def update__city_name(self, new_city_name):
        self.__city_name = new_city_name

    @property
    def get__state_name(self):
        return self.__state_name

    def update_state_name(self, new_state_name):
        self.__state_name = new_state_name

    @property
    def get__country_name(self):
        return self.__country_name

    def update__country_name(self, new_country_name):
        self.__country_name = new_country_name
