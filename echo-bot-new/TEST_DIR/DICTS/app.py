# imports
import json
from cities import get_city
# from users_storage import storage_func

# telegramm stuff

while True:
    try:
        with open("users_storage.db", "r", encoding="utf-8") as f:
            current_storage = json.load(f)
    except FileNotFoundError:
        with open("users_storage.db", "w+", encoding="utf-8") as f:
            current_storage = [user_data.strip() for user_data in f]       
    except json.decoder.JSONDecodeError:
        with open("users_storage.db", "r", encoding="utf-8") as f:
            current_storage = [user_data.strip() for user_data in f]       

    get_city(current_storage)
