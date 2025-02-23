from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    booking_date = db.Column(db.Date, nullable=False)
    booking_start_time = db.Column(db.Time, nullable=False)
    booking_end_time = db.Column(db.Time, nullable=False)
    equipment_type = db.Column(db.String(50))  # 'computer', '3d', or 'laser'
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # in ForeignKey() reference the parent class "User" then the field of the parent class "id"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    userName = db.Column(db.String(150))
    bookings = db.relationship('Booking')
    # in relationship() reference the child