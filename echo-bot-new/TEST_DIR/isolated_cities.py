import requests


def get_user_info(username):
    try:
        if username in list(user_list.keys()):
            used_cities = user_list[username]
            return username, used_cities, user_list
        else:
            user_list.append({username: used_cities})
            return username, used_cities, user_list            

    except NameError:
        user_list = []
        used_cities = []
        user_list.append({username: used_cities})
        return username, used_cities, user_list

print(get_user_info(input("Enter: ")))


url = "https://gist.githubusercontent.com/gorborukov/0722a93c35dfba96337b/raw/435b297ac6d90d13a68935e1ec7a69a225969e58/russia"
response = requests.get(url)
regions_json = response.json()

cities_set = set()
for region in regions_json:
    cities_set.add(region["city"])


    