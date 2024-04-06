**Steps to Run Webpage**

1.  Activate Virtual Environment

<img src="media/image32.png" style="width:6.5in;height:3.48766in" />

2.  Install Requirements for app.py

<img src="media/image8.png" style="width:6.5in;height:3.4832in" />

3.  Run app.py, and move to link
    > [<u>http://127.0.0.1:5000/</u>](http://127.0.0.1:5000/) on the
    > web-page

<img src="media/image16.png" style="width:6.5in;height:3.45833in" />

4.  The Home Page of the Website is loaded

<img src="media/image41.png" style="width:6.5in;height:3.46429in" />

5.  Move to Login window to access the portal

After Login, based on your login credentials you will be redirected to:

1.  Hospitality Staff Portal (Admin/Stakeholder)

> (example - email:
> [<u>admin1@iitgn.ac.in</u>](mailto:admin1@iitgn.ac.in) & password:
> 123456)

2.  IITGN Members Portal (User)

> (example - email:
> [<u>member1@iitgn.ac.in</u>](mailto:member1@iitgn.ac.in) & password:
> 123456)

3.  Current Guest Portal (User)

> (example - email: guest1@gmail.com & password: sC2k5&HS=9"H. )

<img src="media/image14.png" style="width:6.5in;height:3.44132in" />

<img src="media/image23.png" style="width:6.5in;height:3.47908in" />

Hospitality Staff

<img src="media/image15.png" style="width:6.5in;height:3.45833in" />

IITGN Member Dashboard

<img src="media/image30.png" style="width:6.5in;height:3.48629in" />

Current Guest Dashboard

**Screenshots of Successful execution of dynamic operations**

1.  **INSERT**

<!-- -->

1.  Before Inserting Data

<img src="media/image6.png" style="width:6.5in;height:3.47908in" />

Data to be Inserted

<img src="media/image42.png" style="width:6.5in;height:3.48958in" />

Reservation ID only upto 54 entries

2.  After Inserting Data

<img src="media/image36.png" style="width:6.5in;height:3.44976in" />

Reservation Successful Message with Reservation ID

<img src="media/image3.png" style="width:6.5in;height:3.45833in" />

Reservation of ID 55 is added to MySQL database

B. **DELETE**

1.  Before Deleted

<img src="media/image2.png" style="width:6.5in;height:3.45195in" />

We will be deleting Maintenance Request ID=23 to closed

2.  After Update

<img src="media/image21.png" style="width:6.5in;height:3.45833in" />

> Pop-up Indicating Maintenance Request Deleted

<img src="media/image40.png" style="width:6.5in;height:3.44346in" />

> We can See Request ID=23 in Closed Maintenance Requests Section

<img src="media/image24.png" style="width:6.5in;height:3.47917in" />

In SQL Database we can see status for Request ID=23 is updated to
‘closed’

C. **RENAME**

1.  Before Renaming Password of Guest ID=4

<img src="media/image37.png" style="width:6.5in;height:3.45833in" />

Window to Change Password

<img src="media/image7.png" style="width:6.5in;height:3.44346in" />

The initial Password of Guest 4 is ‘newpass’

2.  After Renaming Password for Guest ID=4

<img src="media/image12.png" style="width:6.5in;height:3.45833in" />

Pop Up indicating password change is sucessful

<img src="media/image34.png" style="width:6.5in;height:3.45388in" />

In Database, the password is renamed to ‘appleisbetter’

D. **Where Clause**

1.  Before applying where clause

<img src="media/image38.png" style="width:6.5in;height:3.44792in" />

Generating Incurred Bills where Guest ID=1

<img src="media/image17.png" style="width:6.5in;height:3.44757in" />

We Can See the Incurs_bill table that establishes relationship between
guest_id and bill_id

2.  After applying where clause

<img src="media/image18.png" style="width:6.5in;height:3.47917in" />

We Received a successfully generated popup, and all bills that are
incurred by Guest ID=1

<img src="media/image39.png" style="width:6.5in;height:3.46429in" />

We have segregated the bills that are incurred by Guest ID=1 in MySQL
Database using the ‘where’ statement.

E. UPDATE

1.  Before Update

<img src="media/image25.png" style="width:6.5in;height:3.45656in" />

For Guest who is login to their account for the first time, first_login
= 1

<img src="media/image1.png" style="width:6.5in;height:3.46875in" />

We enter their credentials

2.  After Update

<img src="media/image19.png" style="width:6.5in;height:3.45109in" />

In the MySQL database, the updated value for the first_login column for
guest = 0

<img src="media/image29.png" style="width:6.5in;height:3.45833in" />

For first login the portal requires Guest to change password from
default password

<img src="media/image11.png" style="width:6.5in;height:3.45274in" />

After password is changed login page opens

**Login Views for Website**

1.  **IITGN Member View**

<img src="media/image14.png" style="width:6.5in;height:3.44132in" />

Login Screen of IITGN Member with current reservations

<img src="media/image28.png" style="width:6.5in;height:3.4774in" />

Member could make a reservation

2.  **Current Guests**

<img src="media/image30.png" style="width:6.5in;height:3.48629in" />

Home Screen For Current Guests

<img src="media/image22.png" style="width:6.5in;height:3.48069in" />

Guests Can Make Travel Reservations

<img src="media/image9.png" style="width:6.5in;height:3.4375in" />

Guests can fill out maintenance request forms

<img src="media/image26.png" style="width:6.5in;height:3.43191in" />

Guests can find list of bills incurred

3.  **Hospitality Staff**

<img src="media/image4.png" style="width:6.5in;height:3.46875in" />

Home Page Hospitality Staff, staff can view occupied rooms and
maintenance requests

<img src="media/image10.png" style="width:6.5in;height:3.47357in" />

Staff can view Check-In window where they can check-in Guests

<img src="media/image33.png" style="width:6.5in;height:3.44792in" />

Staff can fill travel requests when requested by guests

<img src="media/image20.png" style="width:6.5in;height:3.46316in" />

Staff can fill and view maintenance request forms filled by guests

<img src="media/image5.png" style="width:6.5in;height:3.47917in" />

Staff can manage and make new reservations

<img src="media/image27.png" style="width:6.5in;height:3.47357in" />

Staff can generate and view bills incurred by guests

4.  **Driver Portal**

<img src="media/image13.png" style="width:6.5in;height:3.44792in" />

Driver’s Portal Dashboard

<img src="media/image31.png" style="width:6.5in;height:3.45439in" />

Assigned Request to a Driver

<u>3. Contributions:</u>

1.  Gaurav Shah (Group Leader)

- Created the design of the webapp for different views

- Created dashboards for different views

- Wrote code for the Backend part of the webapp

2.  Soham Rahatal

- Helped in the Backend part of the webapp; creating some pages for
  > admin (hospitality_staff dashboard)

- Helped in the documentation part of the report

3.  Pratik Agrawal

- Completed the entire website Frontend, using the Bootstrap framework.

- Designed Initial Sketches for the website and user interface.

- Drafted Readme Report with explanations.

4.  <span class="mark">Rohit Srivastava</span>

- <span class="mark">Attended Initial Meeting on website ideation</span>

5.  <span class="mark">Banavath Diraj Naik</span>

- <span class="mark">Attended Initial Meeting on website ideation</span>

6.  <span class="mark">Sohitha Sonalika.</span>

- <span class="mark">Attended Initial Meeting on website ideation</span>

- <span class="mark">Added Contacts in HTML file for initial
  > webpage</span>

7.  <span class="mark">Shivamani</span>

- <span class="mark">Attended Initial Meeting on website ideation</span>

- <span class="mark">Created feedback page for admin
  > (</span>hospitality_staff dashboard) <span class="mark">view</span>

Sub-groups:

G1: Pratik Agarwal, Rohit Srivastav, Banavath Diraj Naik,
<span class="mark">Sohitha Sonalika</span>

G2: Gaurav Shah, Soham Rahatal, <span class="mark">Shivamani</span>

The End

<img src="media/image35.png" style="width:0.53646in;height:0.60352in" />
