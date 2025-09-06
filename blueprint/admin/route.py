from flask import Blueprint, render_template, request, redirect,current_app,url_for, flash
from werkzeug.utils import secure_filename

from datetime import datetime
import os
admins = Blueprint('admin',__name__,template_folder='templates')


@admins.route('/')
def dashboard():
    return render_template('form.html')

@admins.route('/uploads', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'image_file' not in request.files:
            return redirect(url_for('admin.upload_image'))
        file = request.files['image_file']
        if file.filename == '':
            flash("No selected file")
            return redirect(url_for('admin.upload_image'))
        if file and allowed_file(file.filename): # Define allowed_file function
            filename = secure_filename(file.filename)
            upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)
            flash("Image uploaded successfully: {filename}","success")
            return redirect(url_for('admin.upload_image'))
    return render_template('uploads.html')

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']