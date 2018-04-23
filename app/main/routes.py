from flask import render_template,flash,redirect,url_for,request,current_app
from app import  db
from app.main.forms import EditProfileForm,PostForm,CommentForm
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User,Post,Comment
from werkzeug.urls import url_parse
from datetime import datetime
# from app.email import send_password_reset_email
from app.main import bp


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@bp.route('/',methods=['GET', 'POST'])
@bp.route('/index',methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():

        post = Post(body=form.post.data, author=current_user)
        # db.session.add(title)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('main.index'))
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num) \
         if posts.has_prev else None
    return render_template('index.html', title ='Home',posts=posts.items,
        form = form,next_url=next_url,prev_url=prev_url)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.user', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('user.html', user=user, posts=posts.items,
                           next_url=next_url, prev_url=prev_url)

@bp.route('/edit_profile', methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('your changes have been saved')
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title=' Edit Profile', form = form)

@bp.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('main.index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('main.user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('main.user', username=username))

@bp.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('main.index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('main.user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('main.user', username=username))

@bp.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.explore', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.explore', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', title='Explore',
     posts=posts.items,next_url=next_url,prev_url=prev_url)

@bp.route('/post/comment/<int:id>', methods=['GET','POST'])
@login_required
def comment(id):
    posts = Post.query.filter_by(id=id).first()
    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment( comment_body=comment_body.form.data, posts=posts, author=current_user)
        db.session.add(comment)
        db.session.commit()
        flash('your comment has been added')
        return redirect(url_for('main.index', id=post.id ))
    return render_template('index.html', title='Comments', form=form)

@bp.route('/post/<id>', methods=['POST','GET'])
def fullpost(id):
   title= f'Posts'
   post = Post.query.filter_by(id=id).first()
   comment  = CommentForm()
   if comment.validate_on_submit():
       comment = Comment(comment_body = comment.comment_body.data, post_id=id)
       db.session.add(comment)
       db.session.commit()
       print(comment)
       return redirect(url_for('main.fullpost', id=post.id))
   allcomments = Comment.query.all()
   postcomments = Comment.query.filter_by(post_id=id).all()


   return render_template('fullpost.html', title=title, post=post, comment=comment, allcomments=allcomments ,postcomments=postcomments)
