import json


def register_user(user):
    with open("users.json", 'w+') as user_data:
        users_data = json.load(user_data)
    print(json.dump(users_dict, users_data))


register_user(" ")