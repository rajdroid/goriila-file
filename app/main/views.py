from flask import render_template, redirect, send_from_directory, current_app, flash, url_for
from werkzeug.utils import secure_filename
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from . import main
from .. import db
from .forms import FileForm, PasswordForm
from ..models import  Item


@main.route('/', methods=('GET', 'POST'))
def upload():
    """
        root route where initial requests will come to upload
        file to the server with password. On successufull completion
        of requests resource link is generated and displayed to user

    """
    form = FileForm()
    filename = None
    item = None;

    # validate form after submission
    if form.validate_on_submit():
        # retrieve filename present in file field in form
        filename = secure_filename(form.file.data.filename)
        # create path where to store file
        path = 'app/' + current_app.config['UPLOAD_FOLDER'] + '/' + filename
        password = form.password.data
        # save file in created path
        form.file.data.save(path)

        # create single Item instance to add to database
        item = Item(path=path, password=password)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            # if entry already exists with same path than raise error
            flash('File with same name exists', 'error')
            # change filename to None because we are using as successfull
            # updation flag in template
            filename = None;
        else:
            flash('File uploaded successfully', 'info')

    elif len(form.errors) <= 2:
        if 'password' in form.errors:
            flash('Password is Required', 'error')

        if 'file' in form.errors:
            flash('File is Required', 'error')

    return render_template('index.html', form=form, filename=filename, item=item)


@main.route('/<int:id>', methods=('GET', 'POST'))
def fetch(id):
    """
        route to access the resource present in the server. User is first prompted with
        form asking password. If password specified and server is newer than 30 min
        than requested resource will be served

        :param id:
            unique id of file present in server
    """
    form = PasswordForm()
    item = Item.query.filter_by(id=id).first()


    if form.validate_on_submit():
        is_password_matched = item.verify_password(form.password.data)
        delta = datetime.utcnow() - item.time_created

        if is_password_matched:
            # if file is not newer than 30 minutes than display error message
            if delta.seconds/60 > 30:
                flash('File removed from server', 'error')
                return render_template('password_check.html', form=form, item=item)

            # if everything validated correctly than serve the resource to user
            return send_from_directory(current_app.config['UPLOAD_FOLDER'], item.path.split('/')[-1], as_attachment=False)
        else:
            flash('Password Incorrect', 'error')
            return render_template('password_check.html', form=form, item=item)

    # if validation failed than check if user provided password or not
    elif len(form.errors) <= 1 and 'password' in form.errors:
        flash('Password is Required', 'error')

    return render_template('password_check.html', form=form, item=item)
