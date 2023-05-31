from model.models import Request
from dao_interface import RequestIDAO


class RequestDAO(RequestIDAO):
    def __init__(self, session):
        self.session = session

    def insert(self, request: Request):
        self.session.add(request)
        self.session.commit()

    def select(self, request_id):
        return self.session.query(Request).filter(Request.id == request_id).first()

    def update_all(self, request: Request):
        self.session.merge(request)
        self.session.commit()

    def update_status(self, request_id, status):
        request = self.select(request_id)
        if request:
            request.status = status
            self.session.commit()

    def delete(self, request_id):
        request = self.select(request_id)
        if request:
            self.session.delete(request)
            self.session.commit()

    def read_all(self):
        return self.session.query(Request).all()

    def read_by_status(self, status):
        return self.session.query(Request).filter(Request.status == status).all()

    def read_by_user_id(self, user_id):
        return self.session.query(Request).filter(Request.user_id == user_id).all()

    def read_completed(self, user_id):
        return self.session.query(Request).filter(Request.user_id == user_id, Request.status == 'completed').all()
