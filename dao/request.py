from model import *
from dao_interface import RequestIDAO


class RequestDAO(RequestIDAO):
    def __init__(self, connection_pool):
        self.connection_object = connection_pool.get_connection()
        self.mycursor = self.connection_object.cursor()

    def write(self, query, vals):
        try:
            self.mycursor.execute(query, vals)
            self.connection_object.commit()
        except Exception as e:
            print(e)
            print('Write error')

    def read(self, query, vals):
        try:
            self.mycursor.execute(query, vals)
            result = self.mycursor.fetchone()
            return result
        except Exception as e:
            print(e)
            print('Read error')

    def insert(self, request: Request):
        query = "INSERT INTO requests (product_name, product_model, problem_description, user_id, price)" \
                " VALUES (%s, %s, %s, %s, %s)"
        vals = (
            request.product_name, request.product_model, request.problem_description, request.user_id, request.price)
        self.write(query, vals)

    def select(self, request_id):
        query = "select * from users where login = %s and password = %s"
        vals = (request_id,)
        return self.read(query, vals)

    def update(self, request: Request):
        query = 'UPDATE requests SET product_name=%s, product_model=%s, problem_description=%s,' \
                ' status=%s, user_id=%s, price=%s  WHERE id=%s'
        vals = (request.product_name, request.product_model, request.problem_description, request.status,
                request.user_id, request.price, request.id)
        self.write(query, vals)

    def delete(self, request_id):
        query = 'DELETE FROM requests WHERE id=%s'
        vals = (request_id,)
        self.write(query, vals)
