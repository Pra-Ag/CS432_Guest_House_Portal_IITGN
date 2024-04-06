import datetime
from datetime import date
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from sqlalchemy import func
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from forms import BookingForm, CheckInForm, CheckOutForm, MaintenanceRequestForm, TravelRequestForm, LoginForm, RegistrationForm,  enter_guest_idForm
from models import db, current_guest, Room, hospitality_staff, iitgn_member, Reservation, Bill,  maintenance_request, PastGuests, Feedback, travel_request, Assignment, RequiresMaintenance, ManagesMaintenance, ManagesReservation, IncursBill, Makes, GeneratesBill, InitiatedTravelRequest
from random import choices
import string

admin = Blueprint('hospitality_staff_dashboard', __name__)


# @admin.route('/hospitality_staff_dashboard/check_in', methods=['GET', 'POST'])
# @login_required
# def check_in():

#     today = date.today()
#     reservations = Reservation.query.filter(Reservation.check_in_date == today, Reservation.checked_in == False).all()

#     if request.method == 'POST':
#         if 'add_guest' in request.form:
#             reservation_id = request.form['reservation_id']
#             reservation = Reservation.query.get(reservation_id)

#             highest_id = db.session.query(db.func.max(current_guest.guest_id)).scalar()

#             form = CheckInForm()
#             if form.validate_on_submit():
#                 guest = current_guest(
#                     guest_id=highest_id + 1,
#                     first_name=form.first_name.data,
#                     last_name=form.last_name.data,
#                     age=form.age.data,
#                     street=form.street.data, 
#                     state=form.state.data,
#                     pincode= form.pincode.data,    
#                     country=form.country.data,
#                     phone_no=form.phone_no.data,
#                     guest_category=form.guest_category.data,
#                     visit_purpose=form.visit_purpose.data,
#                     iitgn_id=form.iitgn_id.data,  # Do something  about it!
#                     email_id=form.email_id.data,
#                     phone_number=form.phone_number.data,
#                     reservation_id=reservation_id
#                 )
#                 db.session.add(guest)
#                 db.session.commit()
#                 flash('Guest added successfully!', 'success')
#                 if reservation.number_of_people > len(reservation.guests):
#                     if len(reservation.guests) % 2 == 0:
#                         return redirect(url_for('hospitality_staff_dashboard.room_assignment', reservation_id=reservation_id))
#                     return redirect(url_for('hospitality_staff_dashboard.check_in'))
#                 else:
#                     return redirect(url_for('hospitality_staff_dashboard.room_assignment', reservation_id=reservation_id))

#         elif 'assign_room' in request.form:
#             reservation_id = request.form['reservation_id']
#             room_id = request.form['room_id']
#             reservation = Reservation.query.get(reservation_id)
#             room = Room.query.get(room_id)
#             wifi_password = ''.join(choices(string.ascii_letters + string.digits, k=8))
#             for guest in reservation.guests:
#                 guest.room_id = room_id
#                 guest.wifi_password = wifi_password
#                 assignment = Assignment(reservation_id=reservation_id, room_id=room_id, wifi_password=wifi_password)
#                 db.session.add(assignment)
#             db.session.commit()
#             flash(f'Successful Assignment! WiFi Password: {wifi_password}', 'success')
#             return redirect(url_for('hospitality_staff_dashboard.check_in'))

#         elif 'finish_check_in' in request.form:
#             reservation_id = request.form['reservation_id']
#             reservation = Reservation.query.get(reservation_id)
#             reservation.checked_in = True
#             db.session.commit()
#             flash('Successful Check-In!', 'success')
#             return redirect(url_for('hospitality_staff_dashboard'))

#     return render_template('check_in.html', reservations=reservations)

# @admin.route('/hospitality_staff_dashboard/room_assignment/<int:reservation_id>', methods=['GET', 'POST'])
# @login_required
# def room_assignment(reservation_id):

#     reservation = Reservation.query.get_or_404(reservation_id)
#     available_rooms = Room.query.filter(
#         Room.room_type == reservation.room_type,
#         ~Room.room_no.in_([a.room_no for a in Assignment.query.all()])
#     ).all()

#     if request.method == 'GET':
#         reservation = Reservation.query.get_or_404(reservation_id)
#         available_rooms = Room.query.filter(
#             Room.room_type == reservation.room_type,
#             ~Room.id.in_([a.room_id for a in Assignment.query.all()])
#         ).all()
#         return render_template('room_assignment.html', reservation=reservation, available_rooms=available_rooms)

#     if request.method == 'POST':
#         room_id = request.form['room_id']
#         room = Room.query.get(room_id)
#         wifi_password = ''.join(choices(string.ascii_letters + string.digits, k=8))
#         for guest in reservation.guests:
#             guest.room_id = room_id
#             guest.wifi_password = wifi_password
#             assignment = Assignment(reservation_id=reservation_id, room_id=room_id, wifi_password=wifi_password)
#             db.session.add(assignment)
#         db.session.commit()
#         flash(f'Successful Assignment! WiFi Password: {wifi_password}', 'success')
#         return redirect(url_for('hospitality_staff_dashboard.check_in'))

#     return render_template('room_assignment.html', reservation=reservation, available_rooms=available_rooms)
    


# ROUTES FOR CHECK-IN

@admin.route('/hospitality_staff_dashboard/check_in', methods=['GET'])
@login_required
def check_in():

    today = date.today()
    reservations = Reservation.query.filter(Reservation.check_in_date == today, Reservation.checked_in == False).all()
    return render_template('check_in.html', reservations=reservations)

@admin.route('/hospitality_staff_dashboard/add_guest/<int:reservation_id>', methods=['GET', 'POST'])
@login_required
def add_guest(reservation_id):

    i=0

    reservation = Reservation.query.filter_by(reservation_id=reservation_id).first()
    no_of_guests = reservation.number_of_people
    highest_id = db.session.query(db.func.max(current_guest.guest_id)).scalar()

    forms = [ CheckInForm() for _ in range(no_of_guests) ]
    for form in forms:
        if form.validate_on_submit():
            highest_id = db.session.query(db.func.max(current_guest.guest_id)).scalar()
            guest = current_guest(
                guest_id=highest_id + 1,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                age=form.age.data,
                street=form.street.data, 
                state=form.state.data,
                pincode= form.pincode.data,    
                country=form.country.data,
                phone_no=form.phone_no.data,
                guest_category=form.guest_category.data,
                visit_purpose=form.visit_purpose.data,
                iitgn_id=reservation.iitgn_id,  # Do something  about it!
                email_id=form.email_id.data,
                phone_number=form.phone_number.data,
                reservation_id=reservation_id,
                checked_in=True,
                check_out=False
            )
            db.session.add(guest)
            db.session.commit()
            flash(f'Guest added successfully! Guest ID: {highest_id}', 'success')
            i+=1
    if i==no_of_guests:
        return redirect(url_for('hospitality_staff_dashboard.check_in'))
    else:
        return render_template('add_guest.html', forms=forms, no_of_guests=no_of_guests)

@admin.route('/hospitality_staff_dashboard/assign_room/<int:reservation_id>', methods=['GET', 'POST'])
@login_required
def assign_room(guest_id, reservation_id):
    
    #ADD CODE
    
    render_template('assign_room.html')




@admin.route('/hospitality_staff_dashboard/check_out', methods=['GET', 'POST'])
@login_required
def check_out():
    form = CheckOutForm()
    if form.validate_on_submit():
        # Handle check-out form submission
        flash('Guest checked out successfully!', 'success')
        return redirect(url_for('hospitality_staff_dashboard/check_out'))
    return render_template('check_out.html', form=form)

# ROUTES FOR TRAVEL REQUESTS

@admin.route('/hospitality_staff_dashboard/travel_request', methods=['GET', 'POST'])
@login_required
def travel_requests():
    form = TravelRequestForm()
    if form.validate_on_submit():
        # Handle travel request form submission
        highest_id = db.session.query(db.func.max(travel_request.travel_request_id)).scalar()
        if highest_id is None:
            highest_id = 0
        travel_request_new = travel_request(
            travel_request_id=highest_id + 1,
            number_of_travellers=form.number_of_travellers.data,
            date_of_travel=form.date_of_travel.data,
            pick_up_time=form.pick_up_time.data,
            destination=form.destination.data,
            travel_purpose=form.travel_purpose.data
        )

        db.session.add(travel_request_new)
        db.session.commit()
        flash('Travel request submitted successfully!', 'success')
        return redirect(url_for('hospitality_staff_dashboard.travel_requests'))
    return render_template('travel_request.html', form=form)

@admin.route('hospitality_staff_dashboard/travel_request_completed', methods=['GET'])
@login_required
def travel_request_completed():

    completed_travel_requests = travel_request.query.filter_by(driver_license=None).all()
    render_template('travel_request_completed.html', completed_travel_requests=completed_travel_requests)

# ROUTES FOR MAINTENANCE REQUESTS 

@admin.route('/hospitality_staff_dashboard/maintenance_requests', methods=['GET', 'POST'])
@login_required
def maintenance_request_view():

    open_maintenance_requests = maintenance_request.query.filter_by(status='open').all()

    form = MaintenanceRequestForm()

    if form.validate_on_submit():

        highest_id = db.session.query(db.func.max(maintenance_request.request_id)).scalar()
        new_request = maintenance_request(
            request_id = highest_id + 1,
            description = form.description.data,
            date_created = datetime.datetime.now().date(),
            time_created = datetime.datetime.now().time(),
            status='open'
        )
        db.session.add(new_request)
        db.session.commit()
        flash('Maintenance request created successfully!', 'success')
        return redirect(url_for('hospitality_staff_dashboard.maintenance_request_view'))

    
    return render_template('maintenance_request.html', open_maintenance_requests=open_maintenance_requests,
                            form=form)

@admin.route('/hospitality_staff_dashboard/close_maintenance_request/<int:request_id>', methods=['POST'])
@login_required
def close_maintenance_request(request_id):

    maintenance_request_close = maintenance_request.query.get_or_404(request_id)
    maintenance_request_close.status = 'closed'
    db.session.commit()
    flash('Maintenance request closed successfully!', 'success')
    return redirect(url_for('hospitality_staff_dashboard.maintenance_request_view'))

@admin.route('/hospitality_staff_dashboard/maintenance_requests_closed', methods=['GET'])
@login_required
def maintenance_request_closed():

    closed_maintenance_requests = maintenance_request.query.filter_by(status='closed').all()

    return render_template('maintenance_request_closed.html', closed_maintenance_requests= closed_maintenance_requests)

# ROUTES FOR RESERVATIONS

@admin.route('/hospitality_staff_dashboard/booking', methods=['GET', 'POST'])
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
            comments=form.comments.data,
            email_id=form.email_id.data,
            iitgn_id=form.iitgn_id.data,
            checked_in=False,
            checked_out=False
        )

        db.session.add(reservation)
        db.session.commit()
        flash(f'Reservation created successfully! Reservation ID: {reservation.reservation_id}', 'success')
        return redirect(url_for('hospitality_staff_dashboard.booking'))
    return render_template('booking.html', form=form)

@admin.route('/hospitality_staff_dashboard/viewreservations')
@login_required
def viewreservations():

    all_reservations = Reservation.query.all()

    return render_template('viewreservations.html', all_reservations=all_reservations)

# ROUTES FOR BILLS

@admin.route('/hospitality_staff_dashboard/billing', methods=['GET', 'POST'])
@login_required
def billing():
    bill = Bill.query.all()
    form = enter_guest_idForm()
    if form.validate_on_submit():
        # Handle create bill form submission
        guest_id = form.guest_id.data
        
        # Fetch all bill entries for the given guest_id
        incurs_bills = IncursBill.query.filter(IncursBill.guest_id == guest_id).all()
        
        if incurs_bills:
            bill_entries = []
            for incurs_bill in incurs_bills:
                bill_id = incurs_bill.bill_id
                bill_entries += Bill.query.filter_by(bill_id=bill_id).all()
                total_amount = sum(bill_entry.amount for bill_entry in bill_entries)
            flash(f'Bill generated successfully! for guest_id = {guest_id}', 'success')
            return render_template('bill_entries.html', bill_entries=bill_entries, total_amount=total_amount)
        else:
            flash('No bill found for the given guest ID!', 'danger')
            return redirect(url_for('hospitality_staff_dashboard.billing'))
    return render_template('billing.html', bill=bill, form=form)


@admin.route('/hospitality_staff_dashboard/create_bill', methods=['GET', 'POST'])
@login_required
def create_bill():
    form = billForm()

    if form.validate_on_submit():

        highest_id = db.session.query(db.func.max(Bill.bill_id)).scalar()
        new_bill = Bill(
            bill_id = highest_id + 1,
            date_created = datetime.datetime.now().date(),
            time_created = datetime.datetime.now().time(),
            amount = form.amount.data,
            bill_type = form.bill_type.data,
            payment_method = form.payment_method.data,
            paid_status='0',
            generated_by = form.generated_by.data,
            description = form.description.data
        )
        db.session.add(new_bill)
        db.session.commit()
        flash('Bill created successfully!', 'success')
        return redirect(url_for('hospitality_staff_dashboard.create_bill'))
    
    return render_template('create_bill.html', form=form)
