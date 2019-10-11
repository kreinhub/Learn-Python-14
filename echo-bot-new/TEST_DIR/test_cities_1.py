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
        

def game(user_city, used_cities, user_list, checked_letter=False):
    if user_city[0] == checked_letter or not checked_letter:
        if '-' in user_city:
            idx = user_city.find('-')
            user_city = user_city[:idx+1] + user_city[idx+1].upper() + user_city[idx+2:]
        
        exceptions = ["Ы","Ь","Й","Ъ"]
        if user_city not in used_cities:
            if user_city in uniq_cities_list:
                bot_city_first_letter = user_city[-1].upper()
                c = 1
                for i in ''.join(reversed(user_city))[:2]:
                    if i.upper() in exceptions:
                        c += 1
                        bot_city_first_letter = user_city[-c].upper()
                
                # used_cities.append(user_city)
                # for idx, user in enumerate(user_list):
                #     if ''.join(list(user.keys())) == username:
                #         user_list[idx][username].append(user_city)
                #         print(user)

                
                uniq_cities_list.remove(user_city)
                for city in uniq_cities_list:
                    if city.startswith(bot_city_first_letter):
                        bot_city = city
                        # used_cities.append(bot_city)
                        # for idx, user in enumerate(user_list):
                        #     if ''.join(list(user.keys())) == username:
                        #         user_list[idx][username].append(bot_city)
                        #         print(user)
                        
                        uniq_cities_list.remove(bot_city)
                        return bot_city
            else:
                raise ValueError("\tНет такого города в России")

        else:
            return False
    else:
        raise ValueError(f"\tНазвание города должно начинаться с буквы '{checked_letter}'")

url = "https://gist.githubusercontent.com/gorborukov/0722a93c35dfba96337b/raw/435b297ac6d90d13a68935e1ec7a69a225969e58/russia"
response = requests.get(url)
regions_json = response.json()

cities_list = []
for i in regions_json:
    cities_list.append(i["city"])

uniq_cities_list = set(cities_list)


# used_cities = []

while True:
    username = input("Enter your name: ")
    if not username or len(username) <= 3:
        print("\t[Error occured] Entered username is less 4 characters. Enter a valid username")
        continue
    username, used_cities, user_list = get_user_info(username)
    # print(username)
    # print(used_cities)
    # print(user_list)
    # break

    try:
        if used_cities:    
            checked_letter = used_cities[-1][-1].upper()
            user_city = input("Назови город России: ").lower().capitalize()
            bot_city = game(user_city, used_cities, user_list, checked_letter)
            if bot_city:
                # print(user_list)
                for idx, user in enumerate(user_list):
                    if ''.join(list(user.keys())) == username:
                        user_list[idx][username].append(user_city)
                        user_list[idx][username].append(bot_city)
                print(bot_city)
                print(user_list)
            else:
                print("\tЭтот город уже был назван в игре. Ты проиграл")
                break
        else:
            user_city = input("Назови город России: ").lower().capitalize()
            bot_city = game(user_city, used_cities, user_list)
            if bot_city:
                # print(user_list)
                for idx, user in enumerate(user_list):
                    if ''.join(list(user.keys())) == username:
                        user_list[idx][username].append(user_city)
                        user_list[idx][username].append(bot_city)

                print(bot_city)
                print(user_list)
            else:
                print("\tЭтот город уже был назван в игре. Ты проиграл")
                break
    except ValueError as e:
        print(e)