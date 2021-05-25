import os

db_host = os.getenv('DB_HOST',default="localhost")
jwt_secret = "secret"
jwt_algorithm = "HS256"