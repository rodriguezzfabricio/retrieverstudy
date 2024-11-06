from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Course, StudyGroup
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/study')
@login_required  # Require user to be logged in to access the study page
def study():
    # Query the database for all subjects and courses
    subjects = Course.query.with_entities(Course.subject).distinct().all()
    courses = Course.query.all()
    return render_template('study.html', subjects=subjects, courses=courses)

# Add a new profile route
@views.route('/profile')
@login_required
def profile():
    # Pass the current user to the profile page to show user details
    return render_template('profile.html', user=current_user)

# Route to handle checking and displaying existing study groups
@views.route('/check_study_groups', methods=['POST'])
@login_required
def check_study_groups():
    course_id = request.form.get('course')
    selected_course = Course.query.get(course_id)
    study_groups = StudyGroup.query.filter_by(course_id=course_id).all()

    subjects = Course.query.with_entities(Course.subject).distinct().all()
    courses = Course.query.all()

    return render_template('study.html', subjects=subjects, courses=courses, course_selected=True,
                           selected_course=selected_course, study_groups=study_groups)

# Route to handle creating a new study group
@views.route('/create_study_group', methods=['POST'])
@login_required
def create_study_group():
    course_id = request.form.get('course')
    location = request.form.get('location')
    date = request.form.get('date')
    time = request.form.get('time')
    group_size = request.form.get('group_size')

    course = Course.query.get(course_id)
    
    if course:
        new_group = StudyGroup(
            group_name=f"{current_user.name}'s Group for {course.course_name}",
            course_id=course.id,
            location=location,
            date=date,
            time=time,
            max_size=group_size
        )
        db.session.add(new_group)
        db.session.commit()
        flash('Study group created successfully!', category='success')
    else:
        flash('Course not found', category='error')

    return redirect(url_for('views.check_study_groups', course_id=course_id))

@views.route('/join_study_group/<int:group_id>', methods=['POST'])
@login_required
def join_study_group(group_id):
    study_group = StudyGroup.query.get(group_id)
    
    if not study_group:
        flash('Study group not found.', category='error')
        return redirect(url_for('views.study'))

    if current_user in study_group.students:
        flash('You are already a member of this study group.', category='info')
        return redirect(url_for('views.study'))

    if len(study_group.students) >= study_group.max_size:
        flash('This study group is full.', category='error')
        return redirect(url_for('views.study'))

    study_group.students.append(current_user)
    db.session.commit()
    flash('You have successfully joined the study group!', category='success')
    
    return redirect(url_for('views.check_study_groups', course_id=study_group.course_id))

