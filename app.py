from flask import Flask
from blueprint.public.route import views
from blueprint.admin.route import admins
from dotenv import load_dotenv
from flask_mail import Mail, Message
import os
app = Flask(__name__)

load_dotenv()

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
