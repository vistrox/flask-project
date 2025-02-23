from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Booking
from . import db
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/booking/computer', methods=['GET', 'POST'])
@login_required
def booking_computer():
    if request.method == 'POST':
        try:
            # Debug print to see what's being received
            print("Form data:", request.form)
            
            date_str = request.form.get('booking_date')
            start_time_str = request.form.get('booking_start_time')
            end_time_str = request.form.get('booking_end_time')
            booking = request.form.get('booking')  # Changed from 'booking' to 'notes' to match form

            # Debug prints
            print(f"Date: {date_str}")
            print(f"Start Time: {start_time_str}")
            print(f"End Time: {end_time_str}")
            print(f"Computer: {booking}")

            if not all([date_str, start_time_str, end_time_str, booking]):
                raise ValueError("Missing required fields")

            # Convert strings to datetime objects
            booking_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            start_time = datetime.strptime(start_time_str, '%H:%M').time()
            end_time = datetime.strptime(end_time_str, '%H:%M').time()

            new_booking = Booking(
                data=booking,
                booking_date=booking_date,
                booking_start_time=start_time,
                booking_end_time=end_time,
                equipment_type='computer',
                user_id=current_user.id
            )
            
            db.session.add(new_booking)
            db.session.commit()
            flash('Booking successful!', 'success')
            return redirect(url_for('views.home'))

        except ValueError as e:
            print(f"ValueError: {str(e)}")  # Debug print
            flash(f'Invalid date or time format: {str(e)}', 'error')
            return render_template("bookingCom.html", user=current_user)
        except Exception as e:
            print(f"Unexpected error: {str(e)}")  # Debug print
            flash('An error occurred while booking', 'error')
            db.session.rollback()
            return render_template("bookingCom.html", user=current_user)

    return render_template("bookingCom.html", user=current_user)

@views.route('/booking/3d')
@login_required
def booking_3d():

    if request.method == 'POST':
        booking = request.form.get('booking')
        new_booking = Booking(data=booking, user_id=current_user.id)
        db.session.add(new_booking)
        db.session.commit()

    return render_template("booking3D.html", user=current_user)

@views.route('/booking/laser')
@login_required
def booking_laser():

    if request.method == 'POST':
        booking = request.form.get('booking')
        new_booking = Booking(data=booking, user_id=current_user.id)
        db.session.add(new_booking)
        db.session.commit()
        
    return render_template("bookingLaser.html", user=current_user)