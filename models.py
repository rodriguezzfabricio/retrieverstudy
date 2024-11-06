from . import db
from flask_login import UserMixin

# User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user
    email = db.Column(db.String(150), unique=True, nullable=False)  # User's email address (must be unique)
    password = db.Column(db.String(150), nullable=False)  # User's hashed password
    name = db.Column(db.String(150), nullable=False)  # User's full name
    major = db.Column(db.String(150), nullable=True)  # User's major
    year = db.Column(db.Integer, nullable=True)  # User's academic year
    study_groups = db.relationship('StudyGroup', secondary='study_group_members', back_populates='students', lazy='subquery')

# Course Model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each course
    course_name = db.Column(db.String(150), unique=True, nullable=False)  # Name of the course
    student_count = db.Column(db.Integer, nullable=False, default=0)  # Number of students in the course
    subject = db.Column(db.String(150), nullable=False)  # Subject of the course
    study_groups = db.relationship('StudyGroup', backref='course', lazy=True)  # Relationship with study groups

# Association Table for Many-to-Many Relationship between Users and Study Groups
study_group_members = db.Table(
    'study_group_members',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('study_group_id', db.Integer, db.ForeignKey('study_group.id'), primary_key=True)
)

# Study Group Model (keep only this definition)
class StudyGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each study group
    group_name = db.Column(db.String(150), nullable=False)  # Name of the study group
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)  # Link to associated course
    max_size = db.Column(db.Integer, nullable=False, default=8)  # Max size of the study group
    location = db.Column(db.String(150), nullable=False)  # Location of the study group
    date = db.Column(db.String(100), nullable=False)  # Date of the study group
    time = db.Column(db.String(100), nullable=False)  # Time of the study group
    students = db.relationship('User', secondary='study_group_members', back_populates='study_groups', lazy='subquery')  # Many-to-many relationship with users

