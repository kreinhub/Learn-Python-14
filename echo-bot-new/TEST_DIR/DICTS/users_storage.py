# import json

def storage_func(username, city, current_storage):
    if not current_storage:
        if not username and not city:
            return current_storage
        elif type(username) == str and type(city) == str:
            first_user_storage = current_storage
            user_data = {username: [city]}
            first_user_storage.append(user_data)
            # with open("users_storage.db", "w", encoding="utf-8") as f:
            #         f.write(json.dumps(first_user_storage))
            return first_user_storage
        else:
            return False

    elif not username or not city:
        return False

    elif type(username) == str and type(city) == str:
        storage = current_storage
        exist = False
        for idx, user_data in enumerate(current_storage):
            if ''.join(list(user_data.keys())) == username:
                exist = True
                storage[idx][username].append(city)
                # with open("users_storage.db", "w", encoding="utf-8") as f:
                #     f.write(json.dumps(storage))

        if not exist:    
            user_data = {username: [city]}
            storage.append(user_data)
            # with open("users_storage.db", "w", encoding="utf-8") as f:
            #     f.write(json.dumps(storage))
        return storage

    else:
        return False