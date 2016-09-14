from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired


"""
    Class to display file upload form
    :attr file:
        input file field that select file from user's device

    :attr password:
        input password field used for resource access
"""
class FileForm(Form):
    file =  FileField('select file', validators=[FileRequired()])
    password = PasswordField(validators=[DataRequired()]);


"""
    Class to display password form
    :attr password:
        input password field for requested resource

    :attr submit:
        input submit field
"""
class PasswordForm(Form):
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField(label='submit')

