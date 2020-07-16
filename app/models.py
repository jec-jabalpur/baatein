from app import app, db
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from datetime import datetime
from hashlib import md5


followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'),
        lazy='dynamic'
    )

    def __repr__(self):
        return '(User {})'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return app.config['GRAVATAR_SERVICE'].format(digest, size)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed \
            .filter(followers.c.followed_id == user.id) \
            .count() > 0

    def followed_posts(self):
        '''
        self.id -> The intended User
        Objective -> to obtain all the posts of the users that self follows
        Reason -> Because we need to show the posts of users followed by self.

        Post (id, body, timestamp, user_id)
        followers (follower_id, followed_id)
        .
        .
        JOIN Post and followers
        .
        .
        .
        JOIN CONDITION -> (Post.user_id == followers.c.followed_id)
        .
        .
        FILTER
        CRITERIA OF FILTRATION -> self USER is following the author of the posts.
        self.id == followers.c.follower_id
        .
        .
        .
        SORT IN DESCENDING ORDER OF POSTING
        order_by(Post.timestamp.desc())
        '''

        followed_posts = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
            followers.c.follower_id == self.id)

        own_posts = Post.query.filter_by(user_id=self.id)

        return followed_posts.union(own_posts).order_by(Post.timestamp.desc())


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '(Post {})'.format(self.body)

