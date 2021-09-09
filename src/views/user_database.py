import json


def serialize_user(user):
    return {
        user.get__email: {
            "FirstName": user.get__first_name,
            "LastName": user.get__last_name,
            "Password": user.get__password,
            "Username": user.get__user_name
        }
    }


def save_user(user):
    with open("../database/users.json", 'r+', encoding='utf-8') as file_writer:
        user_details: dict = serialize_user(user)
        _dict = json.load(file_writer)
        _dict.update(user_details)
        file_writer.seek(0)
        json.dump(_dict, file_writer, indent=4)
        file_writer.write("\n")


def find_user_by_email(email):
    with open("../database/users.json", 'r+', encoding='utf-8') as file_writer:
        _dict = json.load(file_writer)
        for key in _dict.keys():
            if key == email:
                return True
        return False
