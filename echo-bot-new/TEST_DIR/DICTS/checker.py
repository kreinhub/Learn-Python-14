import requests
import json
import itertools

from users_storage import storage_func 


def find_city(username, city):
    with open("users_storage.db", "r", encoding="utf-8") as f:
        if f.readlines() == []:
            return False
        else:
            f.seek(0)
            for user_data in json.load(f):
                if username == ''.join(list(user_data.keys())):
                    list2d = list(user_data.values())
                    list_of_cities = list(itertools.chain(*list2d))
                    if city in list_of_cities: 
                        return True
            return False