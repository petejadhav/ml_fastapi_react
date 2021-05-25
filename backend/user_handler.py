import psycopg2
import bcrypt
import config
#users =[{'email':"pr@gm.com", 'password':"pwd"}]

class UserDataHandler():
    def __init__(self):   
        self.con = psycopg2.connect(database="testdb", user="postgres", password="postgres", host=config.db_host, port="5432")
        self.cursor = self.con.cursor()
        if self.get_user_count() == 0:
            self.user_db_init_data()
    
    def close(self):
        self.con.close()

    def get_user_count(self):
        query = "select count(*) from public.users"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows[0][0]

    def get_user(self, data: dict):
        query = "select * from public.users where email='{}'".format(data['email'])
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        if len(rows) == 0:
            return []
        return list(rows[0])

    def authenticate_user(self, data: dict):
        if not self.check_user(data):
            return False
        user = self.get_user(data)
        return self.check_password(data['password'], user[2])

    def check_user(self, data: dict):
        if self.get_user(data):
            return True
        return False

    def add_user(self, data: dict):
        if self.check_user(data):
            return False
        data['password'] = self.password_hasher(data['password'])
        self.cursor.execute("INSERT INTO public.users (email,password) VALUES ( '{}', '{}' );".format(data['email'], data['password']))
        self.con.commit()
        return True

    def modify_user(self, data: dict):
        if not self.authenticate_user(data):
            return False
        data['password'] = self.password_hasher(data['password'])
        query = "UPDATE public.users set password = {} where email = {}".format(data['password'],data['email'])
        self.cursor.execute(query)
        self.con.commit()
        return True

    def user_db_init_data(self):
        self.add_user({'email':'pr@gm.com', 'password':'pwd'})

    def password_hasher(self, plain_text_password: str):
        # Hash a password for the first time
        #   (Using bcrypt, the salt is saved into the hash itself)
        return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, plain_text_password, hashed_password):
        # Check hashed password. Using bcrypt, the salt is saved into the hash itself
        return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password.encode('utf-8'))
