from dao_factory import factory


# from connection import get_pool


class User:
    id: int = None
    login: str
    password: str
    role: int = None  # 1- user, 2- admin, 3- master

    def __init__(self, id=None, login=None,  password=None, role=None):
        self.id = id
        self.login = login
        self.password = password
        self.role = role


class Request:
    id: int = None
    product_name: str = None
    product_model: str = None
    problem_description: str = None
    status: str = None  # 'pending', 'accepted', 'rejected', 'completed'
    user_id: int = None
    price: float = None

    def __init__(self, name, model, description, status, user_id, price, request_id=None):
        self.id = request_id
        self.product_name = name
        self.product_model = model
        self.problem_description = description
        self.status = status
        self.user_id = user_id
        self.price = price


class Feedback:
    id: int
    request_id: int = None
    master_id: int = None
    text: str = None

    def __init__(self, id=None, request_id=None, master_id=None, text=None):
        self.id = id
        self.request_id = request_id
        self.master_id = master_id
        self.text = text
