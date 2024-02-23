# Python Flask Project

## Introduction :
 **Flask** is a micro-framework developed by Python that provides only the essential components like _routing_, _request handling_, _session_ & also addtional _modules_ for features such as authentication, database ORM, input validation.
 Flask Framework is **WSGI** complaint hence provides benifits such as flexibility, Interoperability, Scalability & Efficiency.
 This is a simple project which demonstartes 
 - Registration page : Where user can fill details(name, email, password) in form to signup.
 - Login Page : Already registered user can login using username and password
 - Market page: Successfully logged in user can view his/her page which shows a list of items he wishes to buy and his current purse value.
 - Flash messages during success or failure transaction.
  
 I Have configured SQlite3 database to store the data. For that we have to import **SQLAlchemy** to create database instance. SQLAlchemy ilibrary serves as a SQL toolkit and an Object Relational Mapper (ORM).
 Similarly using pip install - we have imported various packages such as **flask_wtf, wtforms, flask_bcrypt, flask_login** which provided useful features that helped in this project.
 Registration/Sign-Up forms uses Flask-WTForms to help with form validation (avoidance of Cross-Site Request Forgery (CSRF)). Hence we have to import **FlaskForm** from wtf_flask lib.
 Template uses Jinja syntax that allows us to access info.
 
 Finally we have a simple Flask Application following MVC architecture i.e a Model file where data communicates with the database, View file which displays the data on the screen & Routes which handles the business logic between View and Model like a controller. 

## How to run project locally:
* Checkout project form git
* Makes sure to have sql db (and know config)
* Open cmd and go to root of the project
* Run command "python" and then import db & ItemName from market
* Create table ItemName in required format using "db.createall()" & ItemName object (eg item1)
* Using db.session.add(item1) and db.session.commit(), get required item list.
* On cmd go to root of project
* Run command "python run.py"

## Home Page:
![FlaskStore_home](https://github.com/PranavMayya/Python_Flask_Store/assets/134544463/684102a7-2b3f-4d46-85ed-9c65ac3510bf)

## Registration form / Signup
![FlaskStore_Signup](https://github.com/PranavMayya/Python_Flask_Store/assets/134544463/90334427-32a8-461d-b11c-abc744cf5163)

## Login page 
![FlaskStore_loginErr](https://github.com/PranavMayya/Python_Flask_Store/assets/134544463/892f5969-f0cd-41e2-8ea2-2fd931274455)

## Market page (LoggedIn page)
![FlaskStor_market](https://github.com/PranavMayya/Python_Flask_Store/assets/134544463/207897a3-0cc5-428e-a214-73688efd40d2)


### Thank You
