from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class Storage:
    
    def __init__(self):
        self.engine = create_engine("postgresql:///users_storage.db")
        self.db = scoped_session(sessionmaker(bind=self.engine))  


    def create_table(self):
        self.query = "CREATE TABLE users(id SERIAL PRIMARY KEY, username VARCHAR NOT NULL, city VARCHAR NOT NULL)"
        self.db.execute(self.query)
        self.conn.commit()

    def create_user(self, username, city):
        self.query = f"INSERT INTO users (username, city) VALUES ({username}, {city})"
        self.cursor.execute(self.query)
        self.conn.commit()

    def update_user_data(self, username, city):
        self.query = f"INSERT INTO users (city) WHERE username = {username} VALUES ({city})"
        self.cursor.execute(self.query)
        self.conn.commit()

    def remove_data(self, username, city):
        self.query = f"DELETE FROM users WHERE username={username}"
        self.cursor.execute(self.query)
        self.conn.commit()

    def select_data(self, username, city):
        self.query = f""
        self.cursor.execute(self.query)
        self.conn.commit()      



