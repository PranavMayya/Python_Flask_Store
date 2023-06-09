from flask import render_template, redirect, url_for, flash, request
from . import app, db
from .models import ItemName, User
from .forms import RegisterForm, LoginForm, PurchaseForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market', methods=['GET','POST'])
@login_required
def market_page():
    purchase_form = PurchaseForm()
    if purchase_form.validate_on_submit():
        print(request.form.get('purchased_item'))
        #p_item_object = ItemName.query.filter_by(name=purchased_item).first()
        #if p_item_object:
         #   p_item_object.owner = current_user.id
          #  current_user.budget -= p_item_object
           # db.session.commit()

    items = ItemName.query.all()
    return render_template('market.html', item_names=items, purchase_form = purchase_form)

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                              email_address = form.email_address.data,
                              password = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully & your logged in as {user_to_create.username}', category='success')
        return redirect(url_for('market_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was error while creating user : {err_msg}')
            
    return render_template('register.html', form=form)

@app.route('/login',methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! your logged in as {attempted_user.username}',category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Incorrect username or password! Please try again',category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out successfully', category='info')
    return redirect(url_for('market_page'))