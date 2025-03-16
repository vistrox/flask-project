from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import ComputerBooking, PrinterBooking, LaserBooking, User  # Update this line
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
            # Get form data
            date_str = request.form.get('booking_date')
            start_time_str = request.form.get('booking_start_time')
            end_time_str = request.form.get('booking_end_time')
            booking = request.form.get('booking')

            if not all([date_str, start_time_str, end_time_str, booking]):
                raise ValueError("Missing required fields")

            # Convert strings to datetime objects
            booking_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            # Just store the time string directly after validating format
            start_time = datetime.strptime(start_time_str, '%H:%M').strftime('%H:%M')
            end_time = datetime.strptime(end_time_str, '%H:%M').strftime('%H:%M')

            new_booking = ComputerBooking(
                computer_number=booking,
                booking_date=booking_date,
                booking_start_time=start_time,
                booking_end_time=end_time,
                user_id=current_user.id
            )
            
            db.session.add(new_booking)
            db.session.commit()
            flash('Booking successful!', 'success')
            return redirect(url_for('views.home'))

        except ValueError as e:
            db.session.rollback()
            flash(f'Invalid date or time format: {str(e)}', 'error')
        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error: {str(e)}")
            flash('An error occurred while booking', 'error')
        finally:
            db.session.remove()  # Use remove() instead of close()

    return render_template("bookingCom.html", user=current_user)

@views.route('/booking/3d', methods=['GET', 'POST'])
@login_required
def booking_3d():
    if request.method == 'POST':
        try:
            # Get form data
            date_str = request.form.get('booking_date')
            start_time_str = request.form.get('booking_start_time')
            end_time_str = request.form.get('booking_end_time')
            booking = request.form.get('booking')
            printer_number = request.form.get('printer_number')

            if not all([date_str, start_time_str, end_time_str, booking]):
                raise ValueError("Missing required fields")

            booking_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            start_time = datetime.strptime(start_time_str, '%H:%M').strftime('%H:%M')
            end_time = datetime.strptime(end_time_str, '%H:%M').strftime('%H:%M')

            new_booking = PrinterBooking(
                printer_model=booking,
                printer_number=printer_number,
                booking_date=booking_date,
                booking_start_time=start_time,
                booking_end_time=end_time,
                user_id=current_user.id
            )
            
            db.session.add(new_booking)
            db.session.commit()
            flash('3D Printer booking successful!', 'success')
            return render_template("booking3D.html", user=current_user)

        except ValueError as e:
            db.session.rollback()
            flash(f'Invalid date or time format: {str(e)}', 'error')
        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error: {str(e)}")
            flash('An error occurred while booking', 'error')
        finally:
            db.session.remove()

    return render_template("booking3D.html", user=current_user)

@views.route('/booking/laser', methods=['GET', 'POST'])
@login_required
def booking_laser():
    if request.method == 'POST':
        try:
            date_str = request.form.get('booking_date')
            start_time_str = request.form.get('booking_start_time')
            end_time_str = request.form.get('booking_end_time')
            booking = request.form.get('booking')
            laser_number = request.form.get('laser_number')

            if not all([date_str, start_time_str, end_time_str, booking]):
                raise ValueError("Missing required fields")

            booking_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            start_time = datetime.strptime(start_time_str, '%H:%M').strftime('%H:%M')
            end_time = datetime.strptime(end_time_str, '%H:%M').strftime('%H:%M')

            new_booking = LaserBooking(
                laser_model=booking,
                laser_number=laser_number,
                booking_date=booking_date,
                booking_start_time=start_time,
                booking_end_time=end_time,
                user_id=current_user.id
            )
            
            db.session.add(new_booking)
            db.session.commit()
            flash('Laser cutter booking successful!', 'success')
            return render_template("bookingLaser.html", user=current_user)

        except ValueError as e:
            db.session.rollback()
            flash(f'Invalid date or time format: {str(e)}', 'error')
        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error: {str(e)}")
            flash('An error occurred while booking', 'error')
        finally:
            db.session.remove()

    return render_template("bookingLaser.html", user=current_user)