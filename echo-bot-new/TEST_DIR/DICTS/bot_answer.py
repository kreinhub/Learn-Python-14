import itertools
import json
import requests

def bot_answer_func(username, user_city, current_storage):
    next_city_letter = user_city[-1][-1].upper()

    url = "https://gist.githubusercontent.com/gorborukov/0722a93c35dfba96337b/raw/435b297ac6d90d13a68935e1ec7a69a225969e58/russia"
    response = requests.get(url)
    regions_json = response.json()
    uniq_cities = {i["city"] for i in regions_json}

    for idx, user_data in enumerate(current_storage):
        if username == ''.join(list(user_data.keys())):
            try:
                list2d = list(user_data.values())
                used_cities = set(itertools.chain(*list2d))
            except TypeError:
                used_cities = set(user_data.values())

            bot_cities = uniq_cities.difference(used_cities)
            for city in bot_cities:
                if city.startswith(next_city_letter):
                    current_storage[idx][username].append(city)
                    storage = current_storage
                    with open("users_storage.db", "w", encoding="utf-8") as f:
                        f.write(json.dumps(storage, ensure_ascii=False))
                    return city