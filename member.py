import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from forms import BookingForm, CheckInForm, CheckOutForm, MaintenanceRequestForm, TravelRequestForm, LoginForm, RegistrationForm, enter_guest_idForm, billForm
from models import db, current_guest, Room, hospitality_staff, iitgn_member, Reservation, Bill, housekeeping_staff, maintenance_request, PastGuests, Feedback, travel_request, driver, Assignment, RequiresMaintenance, ManagesMaintenance, ManagesReservation, IncursBill, Makes, GeneratesBill, InitiatedTravelRequest
from sqlalchemy.orm import joinedload


member = Blueprint('iitgn_member_dashboard', __name__)


@member.route('/iitgn_member_dashboard/booking', methods=['GET', 'POST'])
@login_required
def booking():
    form = BookingForm()
    
    if form.validate_on_submit():
        # Handle booking form submission
        highest_id = db.session.query(db.func.max(Reservation.reservation_id)).scalar()
        if highest_id is None:
            highest_id = 0
        reservation = Reservation(
            reservation_id=highest_id + 1,
            number_of_people=form.number_of_people.data,
            check_in_date=form.check_in_date.data,
            check_out_date=form.check_out_date.data,
            room_type=form.room_type.data,
            specially_enabled_room_required=form.specially_enabled_room_required.data,
            comments=form.comments.data if form.comments.data else ''
        )
        db.session.add(reservation)
        db.session.commit()
        
        # Commit to 'makes' table
        makes_entry = Makes(iitgn_id=current_user.iitgn_id, reservation_id=reservation.reservation_id, comments='')
        db.session.add(makes_entry)
        db.session.commit()    
        
        flash(f'Reservation created successfully! Reservation ID: {reservation.reservation_id}', 'success')
        return redirect(url_for('iitgn_member_dashboard.booking'))
    '''
    specific_member_reservations = db.session.query(Reservation).join(
    Makes, Makes.reservation_id == Reservation.reservation_id).filter(
    Makes.iitgn_id == current_user.iitgn_id).options(joinedload(Reservation.makes)).all()
    return render_template('member_booking.html', form=form, specific_member_reservations=specific_member_reservations)
    '''
    return render_template('member_booking.html', form=form)