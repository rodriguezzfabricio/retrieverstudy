from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required
import hashlib

auth = Blueprint('auth', __name__)  # Blueprint for authentication routes

# Custom hashing and password-checking functions
def hash_password(password):
    """Hashes the given password with SHA-256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def check_password(stored_hash, password_to_check):
    """Compares a stored hashed password with a user-provided plaintext password."""
    return stored_hash == hash_password(password_to_check)

# Render login page
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate login credentials using the User model
        student = User.query.filter_by(email=email).first()

        # Debugging Statements
        if student:
            print("User found:", student.email)
            print("Stored hash:", student.password)
            print("Entered password (hashed):", hash_password(password))

        if student and check_password(student.password, password):
            # Login successful
            flash(f'Welcome, {student.name}!', category='success')
            login_user(student)  # Mark the user as logged in
            return redirect(url_for('views.study'))
        else:
            # Invalid credentials
            flash('Invalid credentials. Please try again.', category='error')
            print("Invalid credentials: email or password incorrect.")

    return render_template('login.html')

# Render logout page
@auth.route('/logout')
@login_required
def logout():
    """Logs out the current user."""
    logout_user()
    flash('You have been logged out.', category='success')
    return redirect(url_for('views.home'))

# Render sign-up page
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        major = request.form.get('major')
        year = request.form.get('year')

        # Validate the form inputs
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif User.query.filter_by(email=email).first():
            flash('Email already exists. Please use a different email.', category='error')
        else:
            # Sign up the user and hash the password before saving it to the database
            hashed_password = hash_password(password1)
            new_user = User(email=email, password=hashed_password, name=name, major=major, year=year)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', category='success')
            return redirect(url_for('auth.login'))  # Redirect to login page after successful sign-up

    return render_template('sign_up.html')
