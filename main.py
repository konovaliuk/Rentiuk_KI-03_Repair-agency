#from dao import UserDAO, RequestDAO, FeedbackDAO, RolesDAO, MastersWorksDAO
from dao import *
from model import *
import mysql.connector
from dotenv import load_dotenv
import os

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

roles_dao = RoleDAO(connection_pool)
roles_dao.insert('user')
roles_dao.insert('admin')
roles_dao.insert('master')


user_dao = UserDAO(connection_pool)
user = User()
user.login = 'user'
user.password = 'qwerty'
user.role = 1
user_dao.insert(user)

user.login = 'admin'
user.password = 'qwerty'
user.role = 2
user_dao.insert(user)

user.login = 'master'
user.password = 'qwerty'
user.role = 3
user_dao.insert(user)

requests_dao = RequestDAO(connection_pool)
request = Request()
request.product_name = 'sony'
request.product_model = '123'
request.problem_description = 'Broken display'
request.user_id = 2
requests_dao.insert(request)

request.status = 'accepted'
request.price = 120
request.id = 1
requests_dao.update(request)

request.status = 'in-work'
requests_dao.update(request)
works_dao = MasterWorkDAO(connection_pool)
works_dao.insert(3, 1)

feedback_dao = FeedbackDAO(connection_pool)
feedback = Feedback()
feedback.request_id = 1
feedback.text = 'Everything works fine now, the repair was fast'
feedback.master_id = 3
feedback_dao.insert(feedback)

request.status = 'completed'
requests_dao.update(request)


