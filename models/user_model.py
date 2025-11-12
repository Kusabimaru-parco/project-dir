from models.db import db
from datetime import datetime, timezone

class User(db.Model):
    __tablename__ = 'users'

    ID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50) )
    Username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    Birthdate = db.Coumn(db.Date)
    Gender = db.Column(db.String(10))
    Phone = db.Column(db.String(20))
    Address = db.Column(db.String(255))
    StudentID = db.Column(db.String(20), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def __repr__(self):
        return f'<User {self.Username}>'

