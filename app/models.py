from app import db
from datetime import datetime

class Phonebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(50), nullable=False)
    last = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(75), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)