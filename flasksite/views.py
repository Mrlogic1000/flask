from flask import Blueprint, render_template


views = Blueprint(__name__, '/')


@views.route("/")
def home():
    return render_template("index.html",active='home')

@views.route("/about")
def about():
    return render_template("about.html",active='about')

@views.route("/contact")
def contact():
    return render_template("contact.html",active='contact')

@views.route("/portfolio")
def portfolio():
    return render_template("portfolio.html",active='portfolio')

@views.route("/services")
def services():
    return render_template("services.html",active='services')