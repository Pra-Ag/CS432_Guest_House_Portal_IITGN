[]{.c22}

[]{.c22}

[![](images/image55.png){style="width: 185.85px; height: 181.27px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 185.85px; height: 181.27px;"}

[]{.c22}

[IITGN Guest House Management System (GHMS)]{.c23 .c45}

------------------------------------------------------------------------

[]{.c22}

[Assignment 4:]{.c26}[ Deploying the DBMS]{.c22}

[]{.c22}

[Team: First Order ]{.c22}

[]{.c22}

[Gaurav Shah - 21110064]{.c22}

[Soham Rahatal - 21110173]{.c22}

[Pratik Agarwal - 21110166]{.c22}

[Rohit Srivastav - 21110180]{.c22}

[Banavath Diraj Naik - 22110044]{.c22 .c21}

[Sohitha Sonalika - 22110151 ]{.c22 .c21}

[Shivamani - 22110062]{.c21 .c26}

[]{.c22}

[]{.c22}

[]{.c22}

[]{.c22}

[]{.c22}

[]{.c22}

[3.1]{.c24}[ Responsibility of G1:]{.c24}

[]{.c23 .c16}

[1.1 Initial Feedback]{.c15}

[]{.c15}

[From the initial feedback by M. Yashwant Chouhan from the Guesthouse,
we have added the following functionalities to our WebApp:\
]{.c5}

1.  [Added changes to the Travel Request Management part of the admin
    dashboard. In the first version of the web app, when a travel
    request is raised by the hospitality staff or the current guest, it
    gets displayed as an unassigned request on the 'Travel Request' page
    of the hospitality_staff dashboard until the driver is not assigned.
    Then, one of the admin users assigns the request to one of the
    drivers by looking at his/her records and the pending requests. This
    version showed the drivers on the available list even when another
    pending request was assigned at the exact pick-up time and date. We
    have fixed this by updating the SQL query, initially fetching the
    list of available drivers by fetching the drivers that don't have a
    pending request ]{.c36}![](images/image1.png)[ to the given
    request.]{.c5}

[]{.c5}

[]{.c23 .c29}

[]{#t.d0b9fae6c57fc544d9690c30382a17b364270b37}[]{#t.0}

+-----------------------------------------------------------------------+
| [    driver_available = \[\]\                                         |
|    ]{.c19 .c25}[for]{.c14}[ drivers ]{.c19                            |
| .c25}[in]{.c14}[ driver_all:\                                         |
|        pending_requests =                                             |
| travel_request.query.filter(travel_request.driver_license ==          |
| drivers.driver_license, travel_request.date_of_travel \>=             |
| request.date_of_travel).all()\                                        |
|        l = len(pending_requests)\                                     |
|        i = ]{.c19 .c25}[0]{.c42 .c40 .c25}[\                          |
|        ]{.c19 .c25}[for]{.c14}[ pending_request ]{.c19                |
| .c25}[in]{.c14}[ pending_requests:\                                   |
|            ]{.c19 .c25}[if]{.c14}[ pending_request.date_of_travel ==  |
| request.date_of_travel ]{.c19                                         |
| .c25}[and]{.c14}[ abs(request.pick_up_time.hour -                     |
| request.pick_up_time.hour) \< ]{.c19 .c25}[6]{.c42 .c40 .c25}[:\      |
|                print(pending_request)\                                |
|                ]{.c19 .c25}[break]{.c14}[\                            |
|            i += ]{.c19 .c25}[1]{.c40 .c25 .c42}[\                     |
|        ]{.c19 .c25}[if]{.c14}[ i == l:\                               |
|            driver_available.append(drivers)\                          |
|    print(driver_available)]{.c19 .c25}                                |
+-----------------------------------------------------------------------+

[]{.c5}

[Before:]{.c11}

[]{.c5}

[![](images/image56.png){style="width: 602.00px; height: 376.02px; margin-left: 0.00px; margin-top: -52.98px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 301.02px;"}

[![](images/image51.png){style="width: 602.00px; height: 375.90px; margin-left: 0.00px; margin-top: -53.90px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 292.92px;"}

[]{.c5}

[![](images/image72.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -54.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 290.00px;"}

[![](images/image46.png){style="width: 601.70px; height: 376.47px; margin-left: 0.00px; margin-top: -55.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 273.33px;"}

[![](images/image60.png){style="width: 601.70px; height: 375.10px; margin-left: 0.00px; margin-top: -53.87px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 277.33px;"}[Both
travel requests get assigned to driver 9.]{.c30}

[After:]{.c11}

[ ]{.c5}

[![](images/image30.png){style="width: 602.00px; height: 375.99px; margin-left: 0.00px; margin-top: -54.99px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 298.99px;"}

[![](images/image24.png){style="width: 602.00px; height: 375.92px; margin-left: 0.00px; margin-top: -55.92px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 278.93px;"}

[]{.c5}

[![](images/image79.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -54.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 293.00px;"}

[![](images/image19.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -54.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 221.00px;"}[![](images/image5.png){style="width: 602.00px; height: 375.86px; margin-left: 0.00px; margin-top: -54.86px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 267.88px;"}

[As the first request is assigned to driver 10, and the second request's
pick-up time is within one hour of the first request, driver 10 is not
on the list of available drivers on the driver assignment page.
Therefore, driver two is selected.]{.c5}

2.  [We have also added a new webpage called 'Room Availability' in the
    hospitality_staff dashboard, enabling the staff to check the room
    availability of the rooms in the guesthouse. This will help the
    staff not to underbook or overbook reservations. Staff can enter a
    date on which he/she wants to see the room availability and then
    will be redirected to a new page where they can see the number of
    rooms available by type. They can't see exactly which room (by its
    number) is available as the room assignment is done at check-in and
    not while reserving. ]{.c5}

[Implemented by creating new routes in admin.py, writing the necessary
SQL queries, and creating the necessary HTML pages.]{.c36}

[]{.c11}

[]{.c11}

[Before:]{.c11}

[]{.c11}

[![](images/image64.png){style="width: 602.00px; height: 375.94px; margin-left: 0.00px; margin-top: -53.94px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 298.95px;"}

[There is no page called "Room Availability" in the initial
version.]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c11}

[After:]{.c11}

[]{.c11}

[![](images/image57.png){style="width: 602.00px; height: 375.93px; margin-left: 0.00px; margin-top: -54.93px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 296.94px;"}

[![](images/image52.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -51.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 182.00px;"}

[![](images/image81.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -52.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 277.00px;"}

[![](images/image59.png){style="width: 602.00px; height: 375.93px; margin-left: 0.00px; margin-top: -49.93px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 143.94px;"}

[Room availability by date can now seen as above. Therefore, the staff
can check whether the requested rooms are available when making a new
reservation.]{.c36}

[]{.c5}

3.  [There wasn't a feedback form page in the current_guest dashboard
    for adding feedback. This has been corrected to allow current guests
    to write about their stay and the submitted feedback can be seen in
    the hospitality_staff dashboard. ]{.c5}

[]{.c5}

[Before:]{.c11}

[]{.c11}

[Current Guest Dashboard]{.c0}

[![](images/image37.png){style="width: 602.00px; height: 375.87px; margin-left: 0.00px; margin-top: -52.87px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 121.89px;"}

[Hospitality Staff Dashboard]{.c0}

[![](images/image18.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -53.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 125.00px;"}

[The current guests can't give their feedback, so the entries in the
"Feedback" page in the hospitality staff's dashboard are NULL.]{.c5}

[]{.c11}

[]{.c11}

[]{.c11}

[After:]{.c11}

[Current Guest Dashboard]{.c47}

[![](images/image15.png){style="width: 602.00px; height: 376.07px; margin-left: 0.00px; margin-top: -55.91px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 143.00px;"}

[![](images/image2.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -54.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 161.27px;"}

[Hospitality Staff Dashboard]{.c0}

[![](images/image23.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -51.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 293.00px;"}

[![](images/image42.png){style="width: 602.00px; height: 376.20px; margin-left: 0.00px; margin-top: -55.96px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 127.47px;"}

[Guests can give feedback from their dashboards, and the hospitality
staff can see them from their dashboards.]{.c5}

[1.2 Final Feedback]{.c15}

[]{.c15}

[As per the final feedback by Mr. Yashwant Chouhan, we have added the
following new features to our database:]{.c5}

[]{.c5}

1.  [Reservation Confirmation for requests made by IITGN members]{.c30
    .c46}

[Initially, when the IITGN Members filled out the reservation form from
their dashboards, a new reservation was directly created without the
approval from the hospitality staff team. To tackle this issue, we have
created a new column in the reservation table in the database called
'confirmed' using the query:        ]{.c5}

[]{.c5}

[]{#t.18a1d289aab0fe74552be65ab21be7527e4f718b}[]{#t.1}

  -------------------------------------------------------------------------------------------------------------------------
  [     alter]{.c41}[ ]{.c19}[table]{.c41}[ reservation ]{.c19}[add]{.c41}[ ]{.c19}[column]{.c41}[ confirmed bool;]{.c19}
  -------------------------------------------------------------------------------------------------------------------------

[]{.c5}

[which will help us track the confirmation status of the reservations.
]{.c5}

[Now, when an IITGN Member creates a reservation, a new reservation does
]{.c5}

[get added to the reservation table, but confirmed = FALSE until the
hospitality staff approves the reservation. Also, if a reservation is
not confirmed and the check-in date exceeds today, it automatically gets
deleted from the reservation table. ]{.c5}

[The reservation made by hospitality staff automatically has confirmed =
TRUE]{.c5}

[]{.c5}

[Before:]{.c11}

[]{.c11}

[]{.c11}

[]{.c11}

[]{.c11}

[]{.c11}

[]{.c11}

[]{.c11}

[]{.c11}

[]{.c11}

[]{.c11}

[]{.c11}

[Reservation form in IITGN Member Dashboard]{.c5}

[![](images/image33.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -52.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 279.00px;"}

[Reservation directly gets made without confirmation]{.c5}

[![](images/image4.png){style="width: 602.00px; height: 375.92px; margin-left: 0.00px; margin-top: -52.92px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 111.93px;"}

[Reservation page in Hospitality Staff's dashboard]{.c5}

[![](images/image63.png){style="width: 602.00px; height: 376.01px; margin-left: 0.00px; margin-top: -57.74px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 291.13px;"}[\
]{.c11}

[After:]{.c11}

[]{.c11}

[]{.c11}

[Reservation form in IITGN Member Dashboard]{.c36}

[![](images/image13.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -52.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 277.00px;"}

[On submission, this creates a reservation request]{.c36}

[![](images/image36.png){style="width: 602.00px; height: 375.92px; margin-left: 0.00px; margin-top: -52.92px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 100.93px;"}

[Home page in IITGN Member Dashboard]{.c5}

[![](images/image48.png){style="width: 602.00px; height: 375.85px; margin-left: 0.00px; margin-top: -54.85px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 149.87px;"}

[Reservation page in Hospitality Staff Dashboard]{.c5}

[![](images/image44.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -52.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 162.00px;"}

[]{.c5}

[]{.c5}

[After clicking on confirm button]{.c5}

[![](images/image62.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -54.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 161.00px;"}

[Home page in IITGN Member Dashboard after reservation
confirmation]{.c5}

[![](images/image26.png){style="width: 602.00px; height: 375.92px; margin-left: 0.00px; margin-top: -51.92px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 165.93px;"}

[]{.c5}

2.  [Room cleaning maintenance request during check-out]{.c30 .c46}

[When a guest checks out, his/her room must be cleaned before it can be
assigned to another guest during check-in. Therefore, we have
implemented this as follows:]{.c5}

1.  [When a current guest checks out, a new maintenance request is
    created: \"CHECK-OUT: Cleaning in room {room_no}."]{.c5}
2.  [A new entry is added to an existing table, 'requires_maintenance,'
    with request_id and room_no.]{.c5}
3.  [This maintenance request is assigned to a housekeeping staff
    following the same procedure as before, but now we have added a new
    page to the housekeeping staff dashboard called "Room Cleaning."
     This will help to keep track of check-out cleaning and other
    maintenance requests easily.]{.c5}
4.  [Until the room cleaning request is closed by the housekeeping staff
    to whom it was assigned, the room is not shown in the list of
    available rooms during the check-in. ]{.c36}

[]{.c5}

[Before:\
]{.c11}

[![](images/image27.png){style="width: 602.00px; height: 376.13px; margin-left: 0.00px; margin-top: -53.02px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 256.90px;"}

[![](images/image82.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -53.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 150.00px;"}

[![](images/image61.png){style="width: 602.00px; height: 375.93px; margin-left: 0.00px; margin-top: -51.93px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 111.94px;"}

[The room checked-out on the same day visible as available room for
check-in ]{.c36}

[![](images/image8.png){style="width: 602.00px; height: 375.85px; margin-left: 0.00px; margin-top: -51.85px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 209.87px;"}

[![](images/image32.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -54.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 110.81px;"}

[]{.c11}

[After:]{.c35}

[]{.c15}

[![](images/image49.png){style="width: 601.70px; height: 376.00px; margin-left: 0.00px; margin-top: -55.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 260.00px;"}[![](images/image77.png){style="width: 602.00px; height: 375.93px; margin-left: 0.00px; margin-top: -52.93px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 156.94px;"}

[Room cleaning maintenance request created automatically]{.c5}

[![](images/image17.png){style="width: 602.00px; height: 375.86px; margin-left: 0.00px; margin-top: -54.86px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 226.88px;"}

[![](images/image74.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -52.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 223.00px;"}

[![](images/image21.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -53.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 298.00px;"}

[]{.c15}

[![](images/image7.png){style="width: 602.00px; height: 375.92px; margin-left: 0.00px; margin-top: -51.92px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 122.93px;"}

[]{.c15}

[]{.c15}

[]{.c15}

[]{.c15}

[]{.c15}

[]{.c15}

[]{.c15}

[Room 112, which was checked out, is not visible in the check-in room
assignment, as the maintenance request hasn't been closed .]{.c5}

[![](images/image53.png){style="width: 602.00px; height: 375.85px; margin-left: 0.00px; margin-top: -53.85px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 227.87px;"}

[![](images/image70.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -55.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 120.00px;"}

[]{.c15}

[Housekeeping Staff Dashboard]{.c5}

[![](images/image11.png){style="width: 602.00px; height: 376.00px; margin-left: 0.00px; margin-top: -54.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 102.00px;"}[![](images/image29.png){style="width: 602.00px; height: 375.93px; margin-left: 0.00px; margin-top: -50.93px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 125.94px;"}[![](images/image25.png){style="width: 602.00px; height: 375.86px; margin-left: 0.00px; margin-top: -54.86px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 119.88px;"}

[]{.c15}

[2. User Views and Privileges in the database]{.c15}

[]{.c15}

1.  [Hospitality Staff Dashboard (Admin) :]{.c30 .c46}

[]{.c30 .c46}

[![](images/image9.png){style="width: 601.70px; height: 320.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 320.00px;"}

[]{.c5}

-   [This hospitality staff dashboard is the home page and we can see
    the options shown above are: ]{.c5}

```{=html}
<!-- -->
```
-   [Check-in: This navigates to the page that shows that day's
    reservations.]{.c5}
-   [Check-out: This navigates to the page that shows that day's
    check-outs and check-out billings.]{.c5}
-   [Travel request: This navigates to the page that shows completed and
    unassigned travel requests.]{.c5}
-   [Maintenance request: This navigates to the page that shows open and
    closed maintenance requests.]{.c5}
-   [Reservations: This navigates to the page that shows all the
    reservations.]{.c5}
-   [Billing: This navigates to the page where we can create or generate
    a Bill.]{.c5}
-   [Feedback: This navigates to the page that shows all the
    feedbacks.]{.c5}
-   [Logout: This can be used to logout from the current account.]{.c5}

[]{.c5}

[]{.c5}

2.  [Current Guest Dashboard:]{.c30 .c46}

[![](images/image71.png){style="width: 601.70px; height: 320.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 320.00px;"}

[        ]{.c5}

-   [This current guest dashboard is the home page of the current guest.
    We can see the options shown above are:]{.c5}

```{=html}
<!-- -->
```
-   [Travel request: This navigates to the page where the guest can make
    a travel request.]{.c5}
-   [Maintenance request: This navigates to the page where the guest can
    make a maintenance request.]{.c5}
-   [Show bills: This navigates to the page that shows all the
    bills]{.c5}
-   [Change password: This navigates to the page where the user can
    change password.]{.c5}
-   [Logout:  This can be used to logout from the current account.]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

3.  [IITGN Member Dashboard:]{.c30 .c46}

[        ]{.c36}[![](images/image12.png){style="width: 601.70px; height: 320.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 320.00px;"}

[]{.c5}

-   [This is the  IITGN member dashboard and we can make a reservation
    through the above shown option.]{.c5}
-   [This current guest dashboard is the home page and the user can
    login with their credentials through the login button shown
    above.]{.c5}

[]{.c5}

4.  [Housekeeping Staff Dashboard:]{.c30 .c46}

[![](images/image6.png){style="width: 601.70px; height: 320.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 320.00px;"}

[]{.c5}

-   [This is the  housekeeping staff dashboard and we can see the
    assigned requests for housekeeping staff through the above shown
    option.]{.c5}
-   [And from the logout option we can logout from the dashboard.]{.c5}

[]{.c5}

5.  [Driver Dashboard:]{.c5}

[![](images/image35.png){style="width: 601.70px; height: 320.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 320.00px;"}

[]{.c5}

-   [This is the  driver dashboard and we can see the assigned requests
    for driver through the above shown option. ]{.c5}
-   [And we can logout through the logout option beside the assigned
    requests option.]{.c5}

[]{.c15}

[ ]{.c15}

[]{.c15}

[]{.c15}

[]{.c15}

[]{.c15}

[]{.c15}

[]{.c15}

[]{.c23 .c16}

[]{.c23 .c16}

[3.2 Responsibility of G2:]{.c6}

[]{.c6}

[1. Concurrent multi-user access]{.c15}

[]{.c5}

[As you may know, our web app has different logins, so different types
of users can access our web app and can modify the database
concurrently. For this, we applied locks for some of our database tables
so that at a time, only a user can update the information, preventing
concurrent transactions from interfering with each other.]{.c5}

[]{.c5}

[For example, guest_travel_request form can be filled by multiple
users/guests. So, we applied locks using SQLAlchemy's (python SQL
toolkit, which is used to manage SQL databases using pythonic language)
support.]{.c5}

[]{.c5}

[![](images/image76.png){style="width: 601.70px; height: 444.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 444.00px;"}

[Code for guest_travel_request page with locking mechanism ]{.c5}

[]{.c5}

[]{.c5}

[For acquiring locks : ]{.c5}

[locked_table = select(travel_request).with_for_update()]{.c23 .c39}

[The above line creates an SQL statement "select \_ \_ \_ for
update"\[6\] that selects rows from the database table 'travel_request'
and acquires a lock on them to prevent any other transaction from being
modified until an existing transaction finishes.]{.c5}

[]{.c5}

[db.session.commit()]{.c39}[: This line commits the changes made within
the transaction to the database and releases the lock acquired
earlier.]{.c5}

[]{.c5}

[To implement concurrent multi-user access, locks have been applied to
the tables like travel_request, guest_travel_request,
maintenance_request, guest_maintenance_request, reservation &
bill.]{.c36}

[]{.c15}

[2. Google Authentication]{.c15}

[]{.c5}

[Our web app has five different logins, and hospitality_staff
(administrator) and iitgn_member are the only ones with an iitgn email
ID. So, we added google authentication for hospitality_staff members and
iitgn_member.]{.c5}

[]{.c5}

[![](images/image22.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[]{.c5}

[When you click on the \[Google Connect\] button to authenticate →]{.c5}

[We are redirected to the page below to select the Google account.]{.c5}

[]{.c5}

[![](images/image16.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[]{.c5}

[After selecting the iitgn account i.e.,
]{.c36}[[sohamrahatal@iitgn.ac.in](mailto:sohamrahatal@iitgn.ac.in){.c38}]{.c35
.c17}

[]{.c5}

[![](images/image50.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[]{.c5}

[We are redirected to the iitgn_member dashboard as my email_id/profile
is present in the iitgn_member database table of our database
'guesthouse_db'.]{.c5}

[]{.c5}

[If an email_id is related to hospitality_staff, then that account will
be redirected to the hospitality_staff dashboard of the web app.]{.c5}

[]{.c5}

[For the rest logins, like driver, guest, and housekeeping_staff, they
will have to login through the normal login system of the web app as
they don't have iitgn email_id.]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[]{.c5}

[3.3 Responsibility of G1 & G2:]{.c6}

[]{.c6}

[1. Attacks on our WebApp]{.c15}

[]{.c15}

1.  [SQL Injection Error Attack:]{.c23 .c34}

[]{.c0}

[![](images/image75.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We try the first method, where we try to add an OR condition that is
always true i.e. 1=1, to modify the SQL query generated through the
form.]{.c0}

[]{.c0}

[![](images/image68.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We received an 'Invalid Credentials' message, and we could not hack
into the system.]{.c0}

[![](images/image38.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We tried the second method, where we used the symbol "\--" which is
used to comment in MySQL. It would comment the SQL code after it, such
that we would be able to hack into the system.]{.c0}

[]{.c0}

[![](images/image65.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We received an 'Invalid Credentials' message, and we could not hack
into the system.]{.c0}

[]{.c0}

[Our System was able to withstand SQL Injection attacks because it uses
parameterized queries, specifically through the ORM (Object-Relational
Mapping) methods provided by the SQLAlchemy library to interact with the
database.]{.c0}

[]{.c0}

2.  [XSS Attack:]{.c23 .c34}

[]{.c0}

[![](images/image10.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We tried to attempt an XSS attack at the login page in our website, if
the attack is successful we would recieve an alert pop-up of
"XSS_Attack!" on web-page.]{.c0}

[]{.c0}

[![](images/image58.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We received an 'Invalid Credentials' message, and we could not conduct
a XSS attack on the login page.]{.c0}

[]{.c0}

[![](images/image45.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[Next we tried to test for XSS attack in admin login where in
Maintenance request form, I entered my own script. Upon sucessfull
attack, we would recieve an alert pop-up of "XSS_Attack!" on the
web-page.]{.c0}

[![](images/image14.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[Our attempt to insert script is failed and the maintenance request form
is submitted with our entered code as plain description text of the
form. We could not conduct a sucessful XSS attack on the admin
page.]{.c0}

[]{.c0}

[We could not conduct XSS attacks sucessfully on our system, because
Flask and its template engine Jinja2 have built-in protections against
XSS. Flask-WTF provides built-in protection against XSS attacks by
automatically escaping HTML entities when rendering form fields and
Jinja2 automatically escapes HTML entities by default when rendering
templates. Moreover, Modern web browsers like Google Chrome also have
built-in XSS protection mechanisms that might prevent certain XSS
attacks from being executed.]{.c0}

[]{.c0}

[]{.c0}

[]{.c0}

[]{.c0}

[]{.c0}

[]{.c0}

[]{.c0}

[]{.c0}

[]{.c0}

[]{.c0}

[]{.c0}

[]{.c0}

[]{.c0}

[]{.c0}

[]{.c0}

3.  [Cross-Site Request Forgery (CSRF) Attack:]{.c23 .c34}

[]{.c0}

[![](images/image69.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[An external site might access the crsf_token for sensitive user
information in the website, like changing passwords in the current guest
account.]{.c0}

[]{.c0}

[![](images/image28.png){style="width: 601.70px; height: 338.99px; margin-left: 0.00px; margin-top: -0.16px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We tried to test if an external site can request to modify the user
data without their information on their behalf.]{.c0}

[]{#t.56bc5a93df0bee3f70963a77ea4a22317acb2a61}[]{#t.2}

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [curl -X POST -H \"X-CSRFToken: ImFhNDMxOTViZTU0YTIyNDY3MzIwNTQ1ZDEwMGQ3OTEzMzNlMzExM2Ei.Zhl6zA.j6K_bhpALVkQ42yENQtwS0QHa4I\" -d \"old_password=abcdef\" -d \"new_password=pass123\" -d \"confirm_password=pass123\" http://127.0.0.1:5000/current_guest_dashboard/change_password]{.c30 .c46}
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[]{.c0}

[We executed the above code to try to change the current password of the
guest ("abcdef") to a new password ("pass123").]{.c0}

[]{.c0}

[![](images/image34.png){style="width: 601.70px; height: 338.99px; margin-left: 0.00px; margin-top: -0.16px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We are unauthorized in changing the password for the user externally,
and their data is protected.]{.c0}

[]{.c0}

[Flask extensions such as Flask-WTF render a CSRF token that is
automatically generated and included in the form. This token is unique
per session and form. Therefore, Flask-WTF automatically adds CSRF
protection to all forms created with it. ]{.c0}

[]{.c0}

4.  [Path Traversal Attack]{.c23 .c34}

[]{.c0}

[![](images/image73.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We are looking that if a housekeeping staff is able to hack into to the
system and access sensitive information of current guests and members
through locally stored files.]{.c0}

[]{.c0}

[![](images/image39.png){style="width: 601.70px; height: 380.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 380.00px;"}

[Code to test for path traversal attack]{.c0}

[]{.c0}

1.  [To test for file traversal attack, we imported the requests
    library, which is a popular Python library that makes HTTP
    requests.]{.c0}
2.  [Setting the target URL: The URL of the web page you\'re testing is
    defined. In this case, it\'s set to
    \']{.c47}[[http://127.0.0.1:5000/hospitality_staff_dashboard](https://www.google.com/url?q=http://127.0.0.1:5000/hospitality_staff_dashboard&sa=D&source=editors&ust=1713109262033350&usg=AOvVaw1HwLdBa2o0uyfFAfGKpF7j){.c38}]{.c17
    .c37}[\'.]{.c0}
3.  [Defining the payloads (../): A list of payloads to test is defined.
    These payloads are common path traversal sequences that attempt to
    move up in the directory structure.]{.c0}
4.  [Getting user input: The script asks for user input. This input is
    expected to be the remaining part of the path after the
    payload]{.c0}
5.  [Sending the requests and checking the responses: The script then
    enters a loop where it iterates over each payload. For each payload,
    it:]{.c0}

```{=html}
<!-- -->
```
1.  [Sends a GET request to the URL with the payload and user input as a
    parameter.]{.c0}
2.  [Prints the response.]{.c0}
3.  [Checks if the response includes sensitive information. If it does,
    it prints a message indicating that the application is vulnerable to
    path traversal. If it doesn\'t, it prints a message indicating that
    the application is not vulnerable to path traversal.]{.c0}

[]{.c0}

1.  [\`etc/passwd\`]{.c0}

[]{.c0}

[This is a Unix file that contains user account information. It should
not be accessible through a web application.]{.c0}

[![](images/image20.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We tried to insert user input to test on the terminal]{.c0}

[]{.c0}

[![](images/image54.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We received an unauthorized error response, and we could not access
sensitive information ]{.c0}

[]{.c0}

[]{.c0}

2.  [\`etc/shadow\`]{.c0}

[![](images/image47.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We tried to insert user input to test on the terminal]{.c0}

[]{.c0}

[![](images/image78.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We received an unauthorized error response, and we could not access
sensitive information ]{.c0}

[ This is another Unix file that contains encrypted password
information. It should also not be accessible.]{.c0}

[]{.c0}

3.  [\`var/www/html/index.html\` ]{.c0}

[]{.c0}

[This is a common location for the main HTML file of a web server. If
you can access this file, it might indicate a path traversal
vulnerability.]{.c0}

[![](images/image66.png){style="width: 601.70px; height: 338.99px; margin-left: 0.00px; margin-top: -0.16px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We tried to insert user input to test on the terminal]{.c0}

[![](images/image67.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We received an unauthorized error response, and we could not access
sensitive information ]{.c0}

[]{.c0}

4.  [4. \`home/\<username\>/.ssh/id_rsa\`]{.c0}

[]{.c0}

[This is the location of the private key for SSH on a Unix system. If
you can access this file, it\'s a serious security vulnerability.]{.c0}

[]{.c0}

[![](images/image40.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We tried to insert user input to test on the terminal]{.c0}

[]{.c0}

[![](images/image80.png){style="width: 601.70px; height: 338.99px; margin-left: 0.00px; margin-top: -0.16px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We received an unauthorized error response, and we could not access
sensitive information ]{.c0}

[]{.c0}

5.  [\`Windows/System32/drivers/etc/hosts\`]{.c0}

[ ]{.c0}

[This is the location of the hosts file on a Windows system. If you can
access this file, it might indicate a path traversal
vulnerability.]{.c0}

[]{.c0}

[![](images/image31.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We tried to insert user input to test on the terminal]{.c0}

[]{.c0}

[![](images/image43.png){style="width: 601.70px; height: 338.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 338.67px;"}

[We received an unauthorized error response, and we could not access
sensitive information ]{.c0}

[]{.c0}

[The Flask web framework, has several built-in features that help
protect against path traversal attacks:]{.c0}

[]{.c0}

[URL Routing]{.c49}[: Flask uses URL routing to map URLs to Python
functions (known as routes). When a request is made to a URL, Flask
executes the corresponding function and returns the result as a
response. This means that the URLs in your application don\'t directly
map to files or directories on your server, which makes path traversal
attacks difficult.]{.c0}

[]{.c0}

[Template Rendering]{.c49}[: Flask uses the Jinja2 template engine to
render views. When you call render_template, Flask looks for the
specified template file in your templates folder, renders it, and
returns the result as a response. This process is safe from path
traversal attacks because Flask doesn\'t expose your file system
structure to the client.]{.c0}

[]{.c0}

[Form Handling]{.c49}[: The request object in Flask provides a secure
way to handle form data. When you call "request.form.get", Flask
retrieves the specified form field from the request. This process is
safe from path traversal attacks because Flask doesn\'t use the form
data to access files or directories on your server.]{.c0}

[]{.c0}

[Database Access: Flask-SQLAlchemy, which you\'re using to interact with
your database, uses SQLAlchemy\'s ORM (Object-Relational Mapping) to map
Python classes to database tables. This means that your database queries
don\'t directly map to files or directories on your server, which makes
path traversal attacks difficult.]{.c0}

[]{.c0}

[Configuration: Flask\'s configuration system allows you to store
sensitive information, like your secret key and database URI, in your
application\'s configuration. This information is not exposed to the
client, which helps protect against path traversal attacks.]{.c0}

[]{.c0}

[]{.c0}

[ 2. Relations and their Constraints from feedback relation with ER
Diagram in Assignment 1]{.c15}

[]{.c5}

[ER Diagram as In Assignment 1]{.c5}

[]{.c1}

[![](images/image41.png){style="width: 601.70px; height: 564.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: -0.00px -0.00px; border: 1.33px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 601.70px; height: 564.00px;"}

[Relationships post Second Feedback]{.c15}

[]{.c15}

[]{#t.109ad29a12228f86704f5bd060f0dde58b8d0ab6}[]{#t.3}

+-----------------------------------------------------------------------+
| []{.c23 .c16}                                                         |
|                                                                       |
| 1.  [Occupancy: current\_]{.c20}[guest ]{.c27}[and ]{.c16}[room       |
|     ]{.c9}                                                            |
|                                                                       |
| []{.c23 .c16}                                                         |
|                                                                       |
| 2.  [affiliation: current\_]{.c20}[guest ]{.c27}[and                  |
|     ]{.c16}[iitgn_member]{.c9}                                        |
|                                                                       |
| []{.c23 .c16}                                                         |
|                                                                       |
| 3.  [booking:]{.c20}[ current_guest ]{.c27}[and                       |
|     ]{.c16}[reservation]{.c9}                                         |
|                                                                       |
| []{.c23 .c16}                                                         |
|                                                                       |
| 4.  [assignment:]{.c20}[ room ]{.c27}[and ]{.c16}[reservation]{.c9}   |
|                                                                       |
| []{.c23 .c16}                                                         |
|                                                                       |
| 5.  [requires_maintainence:]{.c20}[ room ]{.c27}[and                  |
|     ]{.c16}[maintainence_request]{.c9}                                |
|                                                                       |
| []{.c9}                                                               |
|                                                                       |
| 6.  [manages_maintainence:]{.c20}[ hospitality_staff ]{.c27}[and      |
|     ]{.c16}[maintaince_request]{.c9}                                  |
|                                                                       |
| []{.c23 .c16}                                                         |
|                                                                       |
| 7.  [manages_reservation:]{.c20}[ hospitality_staff ]{.c27}[and       |
|     ]{.c16}[reservation]{.c9}                                         |
|                                                                       |
| []{.c16 .c23}                                                         |
|                                                                       |
| 8.  [assigned_to:]{.c20}[ maintaince_request ]{.c27}[and              |
|     ]{.c16}[housekeeping_staff]{.c9}                                  |
|                                                                       |
| []{.c23 .c16}                                                         |
|                                                                       |
| 9.  [incurres_bill:]{.c20}[ guest ]{.c27}[and ]{.c16}[bill]{.c9}      |
|                                                                       |
| []{.c23 .c16}                                                         |
|                                                                       |
| 10. [generates_bill:]{.c20}[ hospitality_staff ]{.c27}[and            |
|     ]{.c16}[bill]{.c9}                                                |
|                                                                       |
| []{.c23 .c16}                                                         |
|                                                                       |
| 11. [travel_Request: current\_]{.c20}[guest ]{.c27}[and               |
|     ]{.c16}[travel_request]{.c9}                                      |
|                                                                       |
| []{.c9}                                                               |
|                                                                       |
| 12. [assigned_driver: ]{.c20}[travel_request ]{.c27}[and              |
|     ]{.c16}[drivers]{.c9}                                             |
|                                                                       |
| []{.c9}                                                               |
|                                                                       |
| 13. [manage_travel_request: hospitality_staff and                     |
|     travel_Request]{.c9}                                              |
|                                                                       |
| []{.c9}                                                               |
|                                                                       |
| 14. [feedback_history: current\_]{.c20}[guest ]{.c27}[and             |
|     ]{.c16}[feedback]{.c9}                                            |
|                                                                       |
| []{.c1}                                                               |
+-----------------------------------------------------------------------+

[]{.c1}

[Validation with ER Diagram]{.c15}

[]{.c1}

[]{#t.e769f443bd0b6f1f38b52684d36e0e9a185f5034}[]{#t.4}

+-----------------------------------------------------------------------+
| 1.  [Occupancy: current_guest and room]{.c1}                          |
|                                                                       |
| [Constraint: The guest is always assigned a room, which may or may    |
| not be assigned to a particular guest.]{.c1}                          |
|                                                                       |
| [Validity: This constraint is present and valid as it allows for the  |
| relationship between the current guest and the room.]{.c1}            |
|                                                                       |
| []{.c1}                                                               |
|                                                                       |
| 2.  [Affiliation: current_guest and iitgn_member]{.c1}                |
|                                                                       |
| [Constraint: A current guest must be affiliated with the IITGN        |
| member.]{.c1}                                                         |
|                                                                       |
| [Validity: This relationship is present and valid, adhering to the    |
| constraint.]{.c1}                                                     |
|                                                                       |
| []{.c1}                                                               |
|                                                                       |
| 3.  [Booking: current_guest and reservation]{.c1}                     |
|                                                                       |
| [Constraint: A current guest must have a reservation under their      |
| name.]{.c1}                                                           |
|                                                                       |
| [Validity: This relationship is present and valid as it allows for    |
| multiple reservations per guest.]{.c1}                                |
|                                                                       |
| []{.c1}                                                               |
|                                                                       |
| 4.  [Assignment: room and reservation]{.c1}                           |
|                                                                       |
| [Constraint: A new room shall be assigned for every single            |
| reservation.]{.c1}                                                    |
|                                                                       |
| [Validity: This relationship is present and valid, allowing for       |
| multiple reservations to be associated with a room.]{.c1}             |
|                                                                       |
| []{.c1}                                                               |
|                                                                       |
| 5.  [Requires_maintenance: room and maintenance_request]{.c1}         |
|                                                                       |
| [Constraint: A room can require maintenance, and there can be         |
| multiple maintenance requests for different rooms.]{.c1}              |
|                                                                       |
| [Validity: This relationship is present and valid, adhering to the    |
| constraint.]{.c1}                                                     |
|                                                                       |
| []{.c1}                                                               |
|                                                                       |
| 6.  [Manages_maintenance: hospitality_staff and                       |
|     maintenance_request]{.c1}                                         |
|                                                                       |
| [Constraint: Hospitality staff can manage multiple maintenance        |
| requests.]{.c1}                                                       |
|                                                                       |
| [Validity: This relationship is present and valid, allowing staff to  |
| manage multiple maintenance requests.]{.c1}                           |
|                                                                       |
| []{.c1}                                                               |
|                                                                       |
| 7.  [Manages_reservation: hospitality_staff and reservation]{.c1}     |
|                                                                       |
| [Constraint: Hospitality staff can manage multiple                    |
| reservations.]{.c1}                                                   |
|                                                                       |
| [Validity: This relationship is present and valid, adhering to the    |
| constraint.]{.c1}                                                     |
|                                                                       |
| []{.c1}                                                               |
|                                                                       |
| 8.  [Assigned_to: maintenance_request and housekeeping_staff]{.c1}    |
|                                                                       |
| [Constraint: Maintenance requests can be assigned to multiple         |
| housekeeping staff members.]{.c1}                                     |
|                                                                       |
| [Validity: This relationship is present and valid, allowing for       |
| multiple staff members to be assigned to maintenance requests.]{.c1}  |
|                                                                       |
| []{.c1}                                                               |
|                                                                       |
| 9.  [Incurs_bill: guest and bill]{.c1}                                |
|                                                                       |
| [Constraint: A guest can incur multiple bills.]{.c1}                  |
|                                                                       |
| [Validity: This relationship is present and valid, allowing for       |
| multiple bills to be associated with a guest.]{.c1}                   |
|                                                                       |
| []{.c1}                                                               |
|                                                                       |
| 10. [Generates_bill: hospitality_staff and bill]{.c1}                 |
|                                                                       |
| [Constraint: Hospitality staff can generate multiple bills.]{.c1}     |
|                                                                       |
| [Validity: This relationship is present and valid, adhering to the    |
| constraint.]{.c1}                                                     |
|                                                                       |
| []{.c1}                                                               |
|                                                                       |
| 11. [Travel_Request: current_guest and travel_request]{.c1}           |
|                                                                       |
| [Constraint: A current guest can have multiple travel requests.]{.c1} |
|                                                                       |
| [Validity: This relationship is present and valid, allowing for       |
| multiple travel requests per guest.]{.c1}                             |
|                                                                       |
| []{.c1}                                                               |
|                                                                       |
| 12. [Assigned_driver: travel_request and drivers]{.c1}                |
|                                                                       |
| [Constraint: A travel request must be assigned to a single            |
| driver.]{.c1}                                                         |
|                                                                       |
| [Validity: This relationship is present and valid, allowing for       |
| drivers to be assigned to a travel request.]{.c1}                     |
|                                                                       |
| []{.c1}                                                               |
|                                                                       |
| 13. [Manage_travel_request: hospitality_staff and                     |
|     travel_request]{.c1}                                              |
|                                                                       |
| []{.c1}                                                               |
|                                                                       |
| [Constraint: Hospitality staff can manage multiple travel             |
| requests.]{.c1}                                                       |
|                                                                       |
| [Validity: This relationship is present and valid, adhering to the    |
| constraint.]{.c1}                                                     |
|                                                                       |
| [Feedback_history: current_guest and feedback]{.c1}                   |
|                                                                       |
| []{.c1}                                                               |
|                                                                       |
| [Constraint: A current guest can have multiple feedback               |
| entries.]{.c1}                                                        |
|                                                                       |
| [Validity: This relationship is present and valid, allowing for       |
| multiple feedback entries per guest.]{.c1}                            |
|                                                                       |
| []{.c1}                                                               |
+-----------------------------------------------------------------------+

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c1}

[]{.c6}

[]{.c6}

[4. Contributions:]{.c6}

[]{.c23 .c16}

1.  [Gaurav Shah (Group Leader)]{.c49 .c53}

-   [Completed all the changes in the WebApp as mentioned in both
    feedbacks.]{.c5}
-   [Created the final report.]{.c5}

[]{.c5}

2.  [Soham Rahatal]{.c49 .c53}

-   [Added locks for some database tables for concurrent multi-user
    access]{.c5}
-   [Added the Google authentication for the admin and iitgn_member
    ]{.c5}
-   [Collected feedback from stakeholders with Gaurav & Pratik]{.c5}
-   [Involved in the drafting of the final report.]{.c5}

[]{.c5}

3.  [Pratik Agrawal]{.c49 .c53}

-   [Conducted tests for SQL Injection, XSS, CRSF, & Path Traversal
    attacks ]{.c5}
-   [Completed Validity of Relationships after feedback with ER
    diagram]{.c5}
-   [Collected feedback from stakeholders with Gaurav & Soham]{.c5}
-   [Involved in the drafting of the final report.]{.c5}

[]{.c5}

4.  [Rohit Srivastava]{.c15 .c21}

-   [NO CONTRIBUTION]{.c5 .c21}

[]{.c5}

5.  [Banavath Diraj Naik]{.c15 .c21}

-   [Q2 in Responsibility for G1 ]{.c36 .c21}

6.  [Sohitha Sonalika]{.c15 .c21}

-   [Q2 in Responsibility for G1 ]{.c5 .c21}

7.  [Shivamani]{.c15 .c21}

-   [Q2 in Responsibility for G1]{.c5 .c21}

[]{.c23 .c16 .c21}

[Sub-groups:]{.c22}

[]{.c22}

[G1:  Pratik Agarwal, Rohit Srivastav, Banavath Diraj
Naik,]{.c36}[ ]{.c36 .c21}[Sohitha Sonalika]{.c47 .c21 .c51}

[G2: Gaurav Shah, Soham Rahatal, ]{.c36}[Shivamani]{.c36 .c21}

[]{.c5 .c21}

[]{.c23 .c16}

[References]{.c26}[:]{.c23 .c16}

[]{.c23 .c16}

1.  [[https://guesthouse.iitgn.ac.in/booking.php](https://www.google.com/url?q=https://guesthouse.iitgn.ac.in/booking.php&sa=D&source=editors&ust=1713109262050917&usg=AOvVaw3WE7K61gbXe43zCTPT0Clc){.c38}]{.c16
    .c17}[ ]{.c23 .c16}
2.  [[https://guesthouse.iitgn.ac.in/accommodation_facility.html](https://www.google.com/url?q=https://guesthouse.iitgn.ac.in/accommodation_facility.html&sa=D&source=editors&ust=1713109262051325&usg=AOvVaw0JSPpzoA3ZWEVm8fi1kcuh){.c38}]{.c16
    .c17}

[]{.c16 .c17 .c32}

[]{.c23 .c16}

------------------------------------------------------------------------

[]{.c23 .c16}

[]{.c23 .c16}

[The End ]{.c23 .c16}

[]{.c23 .c16}

[![](images/image3.png){style="width: 51.50px; height: 57.94px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"}]{style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 51.50px; height: 57.94px;"}

[]{.c23 .c16}

<div>

[]{.c23 .c29}

</div>
