from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.main import bp
from app.models import Student, Achievement
from app.main.forms import StudentForm, AchievementForm
from app import db

@bp.route('/')
@bp.route('/dashboard')
@login_required
def dashboard():
    students = Student.query.all()
    achievements = Achievement.query.order_by(Achievement.created_at.desc()).limit(5).all()
    return render_template('main/dashboard.html', students=students, achievements=achievements)

@bp.route('/students')
@login_required
def students():
    students = Student.query.all()
    return render_template('main/students.html', students=students)

@bp.route('/student/add', methods=['GET', 'POST'])
@login_required
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            reg_number=form.reg_number.data,
            year=form.year.data
        )
        db.session.add(student)
        db.session.commit()
        flash('Student added successfully')
        return redirect(url_for('main.students'))
    return render_template('main/add_student.html', form=form)

@bp.route('/achievements')
@login_required
def achievements():
    achievements = Achievement.query.all()
    return render_template('main/achievements.html', achievements=achievements)

@bp.route('/achievement/add', methods=['GET', 'POST'])
@login_required
def add_achievement():
    form = AchievementForm()
    if form.validate_on_submit():
        achievement = Achievement(
            student_id=form.student_id.data,
            title=form.title.data,
            description=form.description.data,
            date_achieved=form.date_achieved.data
        )
        db.session.add(achievement)
        db.session.commit()
        flash('Achievement added successfully')
        return redirect(url_for('main.achievements'))
    return render_template('main/add_achievement.html', form=form)