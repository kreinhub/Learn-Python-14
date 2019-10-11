import requests
import json

from users_storage import storage_func
from checker import find_city
from bot_answer import bot_answer_func


def get_city(current_storage): 
    username = input("Введи имя пользователя: ")
    city = input("Введи название города: ").lower().capitalize()
    exist = find_city(username, city)
    if not exist:
        storage = storage_func(username, city, current_storage)
        if not storage:
            print("\tНекорректное имя пользователя или название города. Попробуй еще раз")
        else:
            with open("users_storage.db", "w", encoding="utf-8") as f:
                f.write(json.dumps(storage, ensure_ascii=False))
            
            bot_city = bot_answer_func(username, city, storage)
            print(bot_city)
            # debug print
            with open("users_storage.db", "r", encoding="utf-8") as f:
                for i in f:
                    print(i)           

    else:
        with open("users_storage.db", "w+") as f:
            # current_storage = json.load(f)
            current_storage = [user_data.strip() for user_data in f]       
            for user_data in current_storage:
                if ''.join(list(user_data.keys())) == username:
                    current_storage.remove(user_data)           # сработает ли? может по ключу попробовать с pop() и enumerate()?
                    f.write(json.dumps(current_storage, ensure_ascii=False))

        print(f"\tГород <{city}> уже тобой использовался <{username}>. Ты проиграл")
        # debug print
        with open("users_storage.db", "r", encoding="utf-8") as f:
            for i in f:
                print(i)


    # storage = storage_func(username, city, current_storage)
    # if not storage:
    #     print("Not a valid username of city. Try again")
    # else:
    #     bot_answer(username, city, storage)




        # with open("users_storage.db", "r") as f:
        #     for i in f:
        #         print(i)
        

