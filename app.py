from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.sql.functions import user
from models import db, connect_db, User, Post


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://:5433/blogly2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "harrison"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)

@app.route('/')
def list_users():
    """shows list os users in db"""
    users = User.query.all()
    return render_template('home.html', users=users)

@app.route("/add_user")
def new_user_form():

    return render_template('new_user.html')

@app.route('/', methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]
    pos = request.form["position"]
    origin = request.form["origin"]
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url, position=pos, c_of_origin=origin)
    db.session.add(new_user)
    db.session.commit()
    return redirect(f"/{new_user.id}")

@app.route('/delete/<int:user_id>', methods=["POST"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/")

@app.route('/edit/<int:user_id>')
def edit_(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)

@app.route('/edit/<int:user_id>/go', methods=["POST"])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"]
    db.session.add(user)
    db.session.commit()
    return redirect(f"/{user.id}")

@app.route('/<int:user_id>')
def show_user(user_id):
    """show details about a single user"""
    user = User.query.get_or_404(user_id)
    return render_template("detail.html", user=user)

@app.route('/<int:user_id>/new_post')
def post_form(user_id):
    user = User.query.get(user_id)
    return render_template('create_post.html', user=user)

@app.route('/<int:user>/post', methods=["POST"])
def new_post(user):
    title = request.form['title']
    content = request.form['content']
    user_id = user
    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f"/{user}")


@app.route('/<int:user_id>/<int:post_id>')
def post_detail(user_id, post_id):
    post = Post.query.get(post_id)
    return render_template('post.html', post=post)

@app.route('/<int:user_id>/edit/<int:post_id>')
def edit_form(user_id, post_id):
    post = Post.query.get(post_id)
    return render_template("edit_post.html", user=user_id, post=post)

@app.route("update/<user_id>/<post_id>/", methods=["POST"])
def updated_post(user_id, post_id):
    post = Post.query.get_or_404(post_id)
    post.title = request.form["title"]
    post.content =request.form["content"]
    db.session.add(post)
    db.session.commit()
    return redirect(f"{user_id}/{post_id}")

@app.route('/<int:user_id>/delete/<int:post_id>', methods=["POST"])
def delete_post(user_id, post_id):
    del_post = Post.query.get(post_id)
    db.session.delete(del_post)
    db.session.commit()
    return redirect(f"/{user_id}")
