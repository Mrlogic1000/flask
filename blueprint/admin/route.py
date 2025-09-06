from flask import Blueprint, render_template


admins = Blueprint('admin',__name__,template_folder='templates')


@admins.route('/')
def dashboard():
    return render_template('form.html')

@admins.route('/uploads')
def uploads():
    return render_template('uploads.html')