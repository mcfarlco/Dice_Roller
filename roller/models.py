from datetime import *
from roller import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

# db.create_all()
# user_1 = User(username="Testname", email="test@gmail.com", password="password")
# user_2 = User(username="Testname2", email="test@gmail.com2", password="password")
# db.session.add(user_1)
# db.session.add(user_2)
# db.sessoin.commit()
# User.query.all()
# User.query.filter_by(username="EXACT").all()
# User.query.get(ID#)
# user = User.query.filter_by(username="Testname").all()
# user.id # prints 1
# post_1 = Post(title="Title 1", content="Content One", user_id=user.id)
# db.session.add(post_1)
# db.session.commit()
# post = Post.query.first()
# post.user_id # prints 1
# post.author # prints User query
# db.drop_all()
