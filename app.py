from flask import Flask
from models import db
from routes import init_routes
app = Flask(__name__)
app.config.from_object("config")

with app.app_context():
    db.init_app(app)
    db.create_all()


init_routes(app)

if __name__ == "__main__":
    app.run(debug=True, port=5004)
