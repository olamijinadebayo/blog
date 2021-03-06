from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,ValidationError,Email,EqualTo,Length
from app.models import User

class EditProfileForm(FlaskForm):
    username = StringField('Username',validators =[DataRequired()])
    about_me = TextAreaField('About me',validators =[Length(min=0,max=140)])
    submit = SubmitField('Submit')

    def __init__(self,original_username,*args,**kwargs):
        super(EditProfileForm, self).__init__(*args,**kwargs)
        self.original_username = original_username

    def validate_username(self,username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

class PostForm(FlaskForm):
    title = TextAreaField('Enter title',validators =[DataRequired(),Length(min=1,max=30)])
    post = TextAreaField('Enter your blogpost here',validators =[DataRequired(),Length(min=1,max=1000)])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment_body = TextAreaField('write comments',validators =[DataRequired(),Length(min=1,max=40)])
    submit = SubmitField('Submit')
