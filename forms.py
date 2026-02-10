from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, EqualTo, DataRequired, Length

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(3,20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Повтор пароля")])
    submit = SubmitField("Register")