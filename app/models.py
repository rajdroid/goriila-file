from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


"""
    Class to represent single resource.

    :attr id:
        unique id of resource in the database

    :attr path:
        path where file stored in the disk

    :attr password_hash:
        hash value of password specified by user

    :attr time_created (naive):
        time when resource created
"""
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
        """
            Non readable property password
        """
        raise AttributeError('password is not a readable property')

    @password.setter
    def password(self, password):
        """
            compute hash of password and store in field

            :param password:
                password which is specified by user
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
            Verify password specified by user to the one present in
            database.

            :param password:
                password specified by user to access resource
        """
        return check_password_hash(self.password_hash, password)

    def set_path(self, path):
        """
            set the path where resource saved in disk

            :param path:
                path where resource is present
        """
        self.path = path