from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
import email_validator
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Blog Title', validators=[Required()])
    blog = TextAreaField('Write a post')
    submit = SubmitField('submit')

class CommentForm(FlaskForm):
    title = StringField('Comment Title', validators=[Required()])
    comment = TextAreaField('Comment')
    submit = SubmitField('submit') 

class BioForm(FlaskForm):
    bio = TextAreaField('authour')
    submit = SubmitField('submit') 
    
     