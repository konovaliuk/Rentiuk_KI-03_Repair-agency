from model import *
from dao_interface import RequestIDAO


class RequestDAO(RequestIDAO):
    def __init__(self, connection_pool):
        self.connection_object = connection_pool.get_connection()
        self.mycursor = self.connection_object.cursor()

    def write(self, query, vals):
        self.mycursor.execute(query, vals)
        self.connection_object.commit()
        return self.mycursor.lastrowid

    def read(self, query, vals):
        self.mycursor.execute(query, vals)
        result = self.mycursor.fetchone()
        return result

    def insert(self, request: Request):
        query = "INSERT INTO requests (product_name, product_model, problem_description, user_id, price)" \
                " VALUES (%s, %s, %s, %s, %s)"
        vals = (
            request.product_name, request.product_model, request.problem_description, request.user_id, request.price)
        self.write(query, vals)

    def select(self, request_id):
        query = "select * from requests where id=%s"
        vals = (request_id,)
        return self.read(query, vals)

    def update_all(self, request: Request):
        query = 'UPDATE requests SET product_name=%s, product_model=%s, problem_description=%s,' \
                ' status=%s, user_id=%s, price=%s  WHERE id=%s'
        vals = (request.product_name, request.product_model, request.problem_description, request.status,
                request.user_id, request.price, request.id)
        self.write(query, vals)

    def update_status(self, req_id, status):
        query = 'UPDATE requests SET status=%s WHERE id=%s'
        vals = (status, req_id)
        self.write(query, vals)

    def delete(self, request_id):
        query = 'DELETE FROM requests WHERE id=%s'
        vals = (request_id,)
        self.write(query, vals)

    def read_all(self):
        query = "select * from requests"
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def read_by_status(self, status):
        query = "select * from requests WHERE status=%s"
        vals = (status, )
        self.mycursor.execute(query, vals)
        return self.mycursor.fetchall()

    def read_by_user_id(self, user_id):
        query = "select * from requests WHERE user_id=%s"
        vals = (user_id,)
        self.mycursor.execute(query, vals)
        return self.mycursor.fetchall()

    def read_completed(self, user_id):
        query = "SELECT * FROM requests WHERE user_id=%s AND status='completed'"
        vals = (user_id, )
        self.mycursor.execute(query, vals)
        return self.mycursor.fetchall()
