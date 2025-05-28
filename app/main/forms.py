from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Email

class StudentForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    reg_number = StringField('Registration Number', validators=[DataRequired()])
    year = SelectField('Year', choices=[('I', 'First'), ('II', 'Second'), ('III', 'Third'), ('IV', 'Fourth')], validators=[DataRequired()])
    submit = SubmitField('Add Student')

class AchievementForm(FlaskForm):
    student_id = SelectField('Student', coerce=int, validators=[DataRequired()])
    title = StringField('Achievement Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    date_achieved = DateField('Date Achieved', validators=[DataRequired()])
    submit = SubmitField('Add Achievement')