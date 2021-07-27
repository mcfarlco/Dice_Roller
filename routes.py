from flask import *
from flask_sqlalchemy import *
from datetime import *
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '3051ebaedce215701e26a4c5d0d27342'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# db.create_all()
# user_1 = User(username='Testname', email='test@gmail.com', password='password')
# user_2 = User(username='Testname2', email='test@gmail.com2', password='password')
# db.session.add(user_1)
# db.session.add(user_2)
# db.sessoin.commit()
# User.query.all()
# User.query.filter_by(username='EXACT').all()
# User.query.get(ID#)
# user = User.query.filter_by(username='Testname').all()
# user.id # prints 1
# post_1 = Post(title="Title 1", content="Content One", user_id=user.id)
# db.session.add(post_1)
# db.session.commit()
# post = Post.query.first()
# post.user_id # prints 1
# post.author # prints User query
# db.drop_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        'author': 'Corey McFarland',
        'title': 'RGB Roller - 1',
        'content': 'Content - 1',
        'date_posted': 'TBD'
    },
    {
        'author': 'Jane Doe',
        'title': 'RGB Roller - 1',
        'content': 'Content - 2',
        'date_posted': 'TBD'
    },
    {
        'author': 'Jane Doe',
        'title': 'RGB Roller - 1',
        'content': 'Content - 2',
        'date_posted': 'TBD'
    },
    {
        'author': 'Jane Doe',
        'title': 'RGB Roller - 1',
        'content': 'Content - 2',
        'date_posted': 'TBD'
    },
    {
        'author': 'Jane Doe',
        'title': 'RGB Roller - 1',
        'content': 'Content - 2',
        'date_posted': 'TBD'
    },
    {
        'author': 'Jane Doe',
        'title': 'RGB Roller - 1',
        'content': 'Content - 2',
        'date_posted': 'TBD'
    },
    {
        'author': 'Jane Doe',
        'title': 'RGB Roller - 1',
        'content': 'Content - 2',
        'date_posted': 'TBD'
    },
    {
        'author': 'Jane Doe',
        'title': 'RGB Roller - 1',
        'content': 'Content - 2',
        'date_posted': 'TBD'
    },
    {
        'author': 'Jane Doe',
        'title': 'RGB Roller - 1',
        'content': 'Content - 2',
        'date_posted': 'TBD'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/connect")
def connect():
    return render_template('connect.html', title='Connect')


@app.route("/roll")
def roll():
    return render_template('roll.html', title='Roll')


@app.route("/multi-roll")
def multi_roll():
    return render_template('multi-roll.html', title='Multi-Roll')


@app.route("/modifiers")
def modifiers():
    return render_template('modifiers.html', title='Modifiers')


@app.route("/customize")
def customize():
    return render_template('customize.html', title='Customize')


@app.route("/settings")
def settings():
    return render_template('settings.html', title='Settings')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


if __name__ == "__main__":
    app.run(debug=True)
