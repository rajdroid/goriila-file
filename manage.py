import os

from flask_script import Manager, Shell
from app import create_app, db
from app.models import Item


app = create_app(os.getenv('FLASK_CONFIG', default='default'))
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, Item=Item)

# add command 'shell' that open shell with some objects in the context
manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()