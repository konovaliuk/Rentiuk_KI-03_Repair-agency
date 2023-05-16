import mysql.connector
from dotenv import load_dotenv
import os


def get_pool():
    load_dotenv()
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    DATABASE = os.getenv('DATABASE')
    HOST = os.getenv('HOST')
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool",
                                                                  pool_size=5,
                                                                  host=HOST,
                                                                  user='root',
                                                                  password=PASSWORD,
                                                                  database=DATABASE
                                                                  )
    return connection_pool
