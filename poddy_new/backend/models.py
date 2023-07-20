from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    podcasts = db.relationship('Podcast', backref='user', lazy=True)

class Podcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    artwork = db.Column(db.String(120), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    voice_model = db.Column(db.String(120), nullable=False)
    podcasts = db.relationship('Podcast', secondary='podcast_guest', backref=db.backref('guests', lazy='dynamic'))

podcast_guest = db.Table('podcast_guest',
    db.Column('podcast_id', db.Integer, db.ForeignKey('podcast.id'), primary_key=True),
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id'), primary_key=True)
)