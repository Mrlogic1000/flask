from flask import Blueprint, render_template, request, redirect,current_app,url_for, flash,session
from werkzeug.utils import secure_filename

from . import admins

from datetime import datetime
import os


@admins.route('/')
def dashboard():
    if "username" in session:
        return render_template('dashboard.html',username=session['username'])

    return redirect(url_for('auth.login'))

@admins.route('/uploads', methods=['GET', 'POST'])
def upload_image():
    if "username" not in session:
        return redirect(url_for("auth.login"))
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