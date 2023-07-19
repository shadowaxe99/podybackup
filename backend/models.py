from flask_sqlalchemy import SQLAlchemy
from openai_function_call import User

db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name: str) -> "UserModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["UserModel"]:
        return cls.query.all()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'name': self.name, 'age': self.age}