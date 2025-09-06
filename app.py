from flask import Flask
from blueprint.public.route import views
from blueprint.admin.route import admins
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from flask_mail import Mail, Message
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = 'keys'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///auth.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class USER(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

def set_password(self, password):
    self.password_hash = generate_password_hash(password)

def check_password(self, password):
    pass


app.config['UPLOAD_FOLDER'] = 'static/uploads' # Example upload folder
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

app.register_blueprint(views, url_prefix="/" )
app.register_blueprint(admins, url_prefix="/admin" )

print(os.getenv('SCREAT_KEY'))

app.config['MAIL_SERVER']= os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL')
mail = Mail(app)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
