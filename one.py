from flask import Flask
from flask import url_for
from flask import render_template
from app import  get_db_connection,get_user

app= Flask(__name__)
app.config['SECRET_KEY']='your secret key'
# @app.route("/")
# def hello_world():
#     return "<p>Hello,World!<P>"

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login',next='/'))
#     print(url_for('profile',username='John Doe'))
# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_user(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET','POST'))
def create():
    return render_template('create.html') 
