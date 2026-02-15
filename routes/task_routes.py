from flask import render_template, abort, url_for, redirect, flash, Blueprint, request
from sqlalchemy.sql.functions import user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required

from forms import RegisterForm, LoginForm
from models import db, User, Tasks

routes = Blueprint("routes", __name__)

@routes.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Вы успешно прошли регистрацию", "succes")
        return redirect(url_for("routes.login"))
    return render_template("register.html", form=form)

@routes.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Вы вошли в аккаунт!', 'succes')
            return redirect(url_for('routes.profile'))
        else:
            flash('Ввведите верные значения')
    return render_template('login.html', form=form)

@routes.route("/profile")
@login_required
def profile():
    tasks = Tasks.query.all()
    render_template("profile.html", tasks=tasks)

