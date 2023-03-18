"""Data models."""
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    """Data model for user accounts."""

    __tablename__ = "flasklogin-user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    created_on = db.Column(db.DateTime(timezone=True),index=False,unique=False,nullable=True)

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

class Project(db.Model):
    """Data model for user projects"""
    __tablename__='project'
    id = db.Column(
        db.Integer,
        primary_key=True,
        unique=True
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
    # created_on = db.Column(
    #     db.DateTime,
    #     unique=False,
    #     nullable=True
    # )

class Entry(db.Model):
    """Data model for project entry"""
    __tablename__='entry'
    id = db.Column(
        db.Integer,
        primary_key=True,
        unique=True
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
    # created_on = db.Column(
    #     db.DateTime,
    #     unique=False,
    #     nullable=True
    # )
    note = db.Column(
        db.String(1024),
        nullable=False
    )
    durate = db.Column(
        db.Integer,
        unique=False,
        nullable=False
    )