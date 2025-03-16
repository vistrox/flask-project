from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class ComputerBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    computer_number = db.Column(db.String(10))  # e.g., 'C1', 'C2'
    booking_date = db.Column(db.Date, nullable=False)
    booking_start_time = db.Column(db.String(5), nullable=False)
    booking_end_time = db.Column(db.String(5), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class PrinterBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    printer_model = db.Column(db.String(50))  # e.g., 'ender-3-s-1-pro', 'k1'
    printer_number = db.Column(db.Integer)  # e.g., 1, 2, 3
    booking_date = db.Column(db.Date, nullable=False)
    booking_start_time = db.Column(db.String(5), nullable=False)
    booking_end_time = db.Column(db.String(5), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class LaserBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    laser_model = db.Column(db.String(50))  # e.g., 'TS6090L', 'MIT-6040'
    laser_number = db.Column(db.Integer)  # e.g., 1, 2, 3
    booking_date = db.Column(db.Date, nullable=False)
    booking_start_time = db.Column(db.String(5), nullable=False)
    booking_end_time = db.Column(db.String(5), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    userName = db.Column(db.String(150))
    computer_bookings = db.relationship('ComputerBooking', backref='user', lazy=True)
    printer_bookings = db.relationship('PrinterBooking', backref='user', lazy=True)
    laser_bookings = db.relationship('LaserBooking', backref='user', lazy=True)

    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)