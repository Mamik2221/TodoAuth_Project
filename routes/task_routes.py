from flask import render_template, abort, url_for, redirect, flash, Blueprint
from werkzeug.security import generate_password_hash

from forms import RegisterForm
from models import db, User

routes = Blueprint("routes", __name__)

@routes.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.add(user)
        db.commit()
        flash("Вы успешно прошли регистрацию", "succes")
        return redirect(url_for("routes.tasks/login"))
    return render_template("register.html", form=form)

@routes.route("/login")
def login():
    pass