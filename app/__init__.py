from flask import Flask, render_template, request, session, redirect, url_for, flash
from .extensions import db,migrate
from dotenv import load_dotenv

from os import environ

load_dotenv()



def get_settings():
    return environ.get('SETTINGS')

def create_app():

    app = Flask(__name__)

    app.config.from_object(get_settings())

    db.init_app(app)
    migrate.init_app(app,db)
    
    

    from . import models
    from .auth import auth
    from .admin import admins
    from .public import views

    
    app.register_blueprint(views, url_prefix="/" )
    app.register_blueprint(admins, url_prefix="/admin" )
    app.register_blueprint(auth )

   


    return app








