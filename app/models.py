from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    time_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super(Item, self).__init__(**kwargs)


    @property
    def password(self):
        raise AttributeError('password is not a readable property')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_path(self, path):
        self.path = path