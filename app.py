from flask import Flask
from models import db, User
from routes import init_routes
from flask_login import LoginManager
app = Flask(__name__)
app.config.from_object("config")

with app.app_context():
    db.init_app(app)
    db.create_all()
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)



init_routes(app)

if __name__ == "__main__":
    app.run(debug=True, port=5004)
