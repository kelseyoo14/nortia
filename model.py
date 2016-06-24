"""Models and database functions for My Life Rhythm project."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


##############################################################################
# Model definitions


class User(db.Model):
    """Time Watcher User"""

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(200), nullable=False)

class Subject(db.Model):
    """User main subjects to track"""

    subject_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(200), nullable=False)


class Topic(db.Model):
    """Topics within subjects to track"""

    topic_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
