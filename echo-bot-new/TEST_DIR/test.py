# def get_user_info(username, city):
#     try:
#         exist = False
#         for idx, user_dict in enumerate(users_storage):
#             if username in ''.join(list(user_dict.keys())):
#                 users_storage[idx][username].append(city)
#                 exist = True

#         if not exist:
#             users_storage.append({username: [city]})

#         return users_storage           


#     except UnboundLocalError:
#         users_storage = []
#         users_storage.append({username: [city]})
#         return users_storage

# def storage():
#     users_storage = []
#     return users_storage

# def get_users_info(username, users_storage):
#     pass

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class Storage:
    
    def __init__(self):
        self.engine = create_engine("postgresql:///users_storage.db")
        self.db = scoped_session(sessionmaker(bind=engine))  


    def create_db(self):
        self.cursor.execute("""CREATE TABLE users(id SERIAL PRIMARY KEY, username VARCHAR NOT NULL, city VARCHAR NOT NULL)""")
        self.conn.commit()

    def create_user(self, username, city):
        self.query = f"INSERT INTO users (username, city) VALUES ({username}, {city})"
        self.cursor.execute(self.query)
        self.conn.commit()

    def update_user_data(self, username, city):
        self.query = f"INSERT INTO users (city) WHERE username = {username} VALUES ({city})"
        self.cursor.execute(self.query)
        self.conn.commit()

    def remove_data(self):
        pass


while True:
    username = input("Enter your name: ")
    city = input("Enter city: ")