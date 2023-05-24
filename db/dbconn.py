import pymysql
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def connect_db():
    return pymysql.connect(
        
        host="localhost", user = os.getenv('DB_USERNAME'), passwd = os.getenv('DB_PASSWORD'), database = os.getenv('DATABASE'),
        autocommit = True, charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor)