from models.db import db
from datetime import datetime, timezone

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    mname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    pass_word = db.Column(db.String(512))
    birthday = db.Column(db.Date)
    gender = db.Column(db.String(10))
    phonenumber = db.Column(db.String(20))
    address = db.Column(db.String(200))
    student_id = db.Column(db.String(20), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def __repr__(self):
        return f'<User {self.username}>'