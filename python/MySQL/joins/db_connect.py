import mysql.connector
from config import db_config

def get_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print("Connection error : ", err)
        return None