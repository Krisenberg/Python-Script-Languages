from flask import Blueprint
from flask_login import (current_user, login_required,
                         login_user, logout_user)
from model.models import User, SpotiClient
from flask import render_template, url_for, flash, redirect, request
from controller.users_forms import (ChooseNewPasswordForm, RegistrationForm,
                                    LoginForm, RequestPasswordResetForm,
                                    UpdateAccountForm)
from app import db, bcrypt, login_manager

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
@login_manager.user_loader
def register():
    if current_user.is_authenticated:
        flash('You are already logged in', category="info")
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pswd = (
            bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        )
        user = User(
            username=form.username.data,
            password=hashed_pswd
            )
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. Please log in.', "success")
        return redirect(url_for('users.login'))
    
    return render_template('register.html', form=form, css_path='static\\css\\main_page.css')


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in', category="info")
        return redirect(url_for('main.home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if (user and bcrypt.check_password_hash(user.password,form.password.data)):
            login_user(user=user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('You are now logged in', category="success")
            return (
                redirect(next_page) if next_page else redirect(url_for('main.home'))
            )
        flash('Login unsuccessful. Please check username and password', category="danger")
    return render_template('login.html', form=form, css_path='static\\css\\main_page.css')


@users.route('/logout')
def logout():
    logout_user()
    flash('You are now logged out', category="info")
    return redirect(url_for('main.home'))


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        # favorite_cameras = Camera.query.filter(
        #     Camera.id.in_(form.favorite_cameras.data)
        #     ).all()
        # current_user.favorite_cameras = favorite_cameras
        db.session.commit()
        flash('Your account has been updated', category="success")
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        # form.favorite_cameras.data = [
        #     camera.id for camera in current_user.favorite_cameras
        #     ]

    return render_template(
        'account.html',
        form=form,
        css_path='static\\css\\users_styling.css'
        # cameras=(Camera.query.all()
        #          if current_user.is_premium
        #          else Camera.query.filter_by(is_premium=False).all())
        )