import logging
import requests


def get_city(bot, update):
    try:
        url = "https://gist.githubusercontent.com/gorborukov/0722a93c35dfba96337b/raw/435b297ac6d90d13a68935e1ec7a69a225969e58/russia"
        response = requests.get(url)
        regions_json = response.json()
    except requests.RequestException:
        logging.info("[Network Error] remote host is unreached")

    cities_list = []
    for i in regions_json:
        cities_list.append(i["city"])

    uniq_cities_list = set(cities_list)

    username = update.message.chat.first_name

    
    used_cities = []
    try:
        if used_cities:    
            checked_letter = used_cities[-1][-1].upper()
            raw_list = update.message.text.split()
            user_city = raw_list[1].lower().capitalize()
            logging.info(f"/cities is called with arg: {user_city}")

            bot_city = game(user_city, used_cities, uniq_cities_list, checked_letter)
            if bot_city:
                logging.info(f"bot answers: {bot_city}")                
                update.message.reply_text(bot_city)

            else:
                bot_answer = "Этот город уже был назван в игре. Ты проиграл"
                logging.info(f"[Error occured] {bot_answer}")
                update.message.reply_text(bot_answer)
                
        else:
            raw_list = update.message.text.split()
            user_city = raw_list[1].lower().capitalize()
            logging.info(f"/cities is called with arg: {user_city}")    

            bot_city = game(user_city, used_cities, uniq_cities_list)
            if bot_city:
                logging.info(f"bot answers: {bot_city}")                
                update.message.reply_text(bot_city)
            else:
                bot_answer = "Этот город уже был назван в игре. Ты проиграл"
                logging.info(f"[Error occured] {bot_answer}")
                update.message.reply_text(bot_answer)
            
    except ValueError as e:
        logging.info(f"[Error occured] {e}")
        update.message.reply_text(str(e))
        

def game(user_city, used_cities, uniq_cities_list, checked_letter=False):
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
                
                used_cities.append(user_city)
                uniq_cities_list.remove(user_city)
                for city in uniq_cities_list:
                    if city.startswith(bot_city_first_letter):
                        bot_city = city
                        used_cities.append(bot_city)
                        uniq_cities_list.remove(bot_city)
                        return bot_city
            else:
                raise ValueError("Нет такого города в России")

        else:
            return False
     else:
         raise ValueError(f"Название города должно начинаться с буквы '{checked_letter}'")