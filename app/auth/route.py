from . import auth
from flask import redirect,request, session, flash, render_template, url_for
from ..models.user import User
from ..extensions import db


@auth.route('/login', methods =["GET","POST"])
def login():
    username = ""
    password = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['username'] = username
            return redirect(url_for('admin.dashboard'))
        else:
            flash("The user does not exist", "error")
            return render_template('login.html')
    return render_template("login.html",username=username)

@auth.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username == "" and password == "":
            flash("The input cannot be empty", "error")
            return render_template('login.html')
        user = User.query.filter_by(username=username).first()
        if user:
            flash("The username has been taken", "error")
            return render_template('login.html')
        else:
            new_username = User(username=username)
            new_username.set_password(password)
            db.session.add(new_username)
            db.session.commit()
            session['username'] = username
        flash("The user added successfully", "success")
        return render_template('login.html')
    return render_template('register.html')


@auth.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("auth.login"))
