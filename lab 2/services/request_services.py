from connection import get_pool
from dao_factory import factory
from model import *


class RequestServices:
    pool = get_pool()
    dao_factory = factory.DaoFactory(pool)
    request_dao = dao_factory.get_dao_implementation('request')

    def add_request(self, request: Request):
        try:
            self.request_dao.insert(request)
            return True
        except:
            return False

    def update_status(self, request_id, status):
        try:
            self.request_dao.update_status(request_id, status)
            return True
        except:
            return False

    def show_by_status(self, status):
        try:
            return self.request_dao.read_by_status(status)
        except:
            return False

    def get_by_user_id(self, id):
        try:
            return self.request_dao.read_by_user_id(id)
        except:
            return False

    def get_by_id(self, id):
        try:
            return self.request_dao.select(id)
        except:
            return False

    def requests_to_feedback(self, user_id):
        try:
            return self.request_dao.read_completed
        except:
            return False
