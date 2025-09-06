from flask import Blueprint, render_template, send_file
from .dbs import educations, experiences, works


views = Blueprint('views',__name__, template_folder='templates')


@views.route("/")
def home():
    return render_template("index.html",active='home')







@views.route("/about")
def about():
    return render_template("about.html",active='about', educations=educations, experiences = experiences)

@views.route("/contact")
def contact():
    return render_template("contact.html",active='contact')

@views.route("/portfolio")
def portfolio():
    return render_template("portfolio.html",active='portfolio')

@views.route("/services")
def services():
    return render_template("services.html",active='services', works=works)

@views.route("/download")
def download_file():
    file = "myResume.pdf"
    return send_file(file, as_attachment=True)