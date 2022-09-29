"""Data models."""
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """Data model for user accounts."""

    __tablename__ = 'flasklogin-users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False
    )
    bio = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )
    admin = db.Column(
        db.Boolean,
        index=False,
        unique=False,
        nullable=False
    )

class Project(db.Model):
    """Data model for user projects"""

    __tablename__='projects'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )
    name = db.Column(
        db.String(64),
        unique=True,
        nullable=False
    )
    description = db.Column(
        db.String(120),
    )
    category = db.Column(
        db.String(32),
        unique=True,
        default='Uncategorized'
    )
    created = db.Column(
        db.Datetime,
        unique=False,
        nullable=False
    )

class Entry(db.Model):
    """Data model for project entry"""

    __tablename__='entry'
    id = db.Column(
        db.Integer,
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )
    project_id = db.Column(
        db.Integer,
        db.ForeignKey('project.id'),
        nullable=False
    )
    created = db.Column(
        db.Datetime,
        unique=False,
        nullable=False
    )
    note = db.Column(
        db.String(1024),
        nullable=False
    )
    durate = db.Column(
        db.Integer,
        unique=False,
        nullable=False
    )

def set_password(self, password):
    """Create hashed password"""
    self.password = generate_password_hash(
        password,
        method='sha256'
    )

def check_password(self, password):
    """Check hashed password"""
    return check_password_hash(self.password, password)

def __repr__(self):
    return '<User {}>'.format(self.username)