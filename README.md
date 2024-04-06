# IITGN Guesthouse Mnagement System
 WebApp created using Flask, MySQL & Python to manage day-to-day taks at IIT Gandhinagar's Guest House

## Pre-Requisites

Open the MySQL Workbench import the 'guesthouse_db.sql' file.

In the `app.py` file, update the line `app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:<password>@localhost/guesthouse_db'` by replacing `<password>` to Mysql server password. 


## Steps to run the Repository

1. Open the directory in the code editor.

2. Now, we need to create a virtual python environment in the project directory. This can be done by executing following commands (windows):
```
python -m venv env
```
```
 .\env\Scripts\activate
```



3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```


4. Run the application:
    ```
    python app.py
    ```
    or

    ```
    flask run
    ```

5. Open your web browser and visit `http://127.0.0.1:5000` to access the application.
