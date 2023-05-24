from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, EmailField, ValidationError
from wtforms.validators import length, Email, EqualTo, DataRequired
from .models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('username already exit! please try another username!')

    def email_validation(self,email_to_check):
        email = User.query.filter_by(email_address=email_to_check.data).first()
        if email:
            raise ValidationError('Email address already exit! please try again using different mail!')

    username = StringField(label='User Name:', validators=[length(min=2,max=30), DataRequired()])
    email_address = StringField(label='Your Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Create Password:', validators=[length(min=5), DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Register/Submit')

class LoginForm(FlaskForm):

    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')

class PurchaseForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')