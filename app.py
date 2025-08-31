from flask import Flask
from views import views
from dotenv import load_dotenv
from flask_mail import Mail, Message
import os
app = Flask(__name__)

load_dotenv()
app.register_blueprint(views, url_prefix="/" )

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
