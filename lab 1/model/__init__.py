import datetime


class User:
    id: int = None
    login: str
    password: str
    role: int  # 1- seller, 2- buyer, 3- admin

    def __str__(self):
        return f"User id: {self.id}, login: {self.login}, password_hash: {self.password}," \
               f"user's role: {self.role} "


class Request:
    id: int
    product_name: str = None
    product_model: str = None
    problem_description: str = None
    status: str = None  # 'pending', 'accepted', 'rejected', 'completed'
    user_id: int = None
    created_at: datetime = None
    price: float = None

    def __str__(self):
        return None


class Feedback:
    id: int
    request_id: int = None
    master_id: int = None
    text: str = None
    created_at: datetime = None

    def __str__(self):
        return f"Edition id: {self.id}, edition year {self.year}," \
               f"label id {self.label_id}, is it remastered {self.is_remastered}, price: {self.price}"
