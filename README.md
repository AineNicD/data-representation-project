# Data Representation Big Project

This repository contains my submission for the Big Project assessment in Data Representation.
# Pythonanywhere link: 
- Pythonanywhere needs reloading at times for the tables to display. I am working on figuring out if this is an error in my code on python anywhere or a problem with python anywhere itself. 
## Project description: 
~~~
Write a program that demonstrates that you understand creating and consuming 
RESTful APIs. 
(Andrew Beatty)
~~~ 

## Repository files:

- [app.py]() - A Flask server that has a REST API that performs CRUD operations. 
- [init.sql]() which contains the SQL code to create the database Vaccination, that has two tables, recipients and vaccinators. There is a third table called users that was used to create the users for authorisation logging in.
- [dbconfig.py]() - A configuration file for the SQL database.
- A data access object file called [VaccinationDao]() which contains CRUD operations for both tables within the Vaccination database. 
- [templates/base.html]() contains the base html for the web pages. 
- [templates/index.html]() contains the html for the homepage. 
- [templates/login]() contains the html for the login form.  For the purpose of the project the username and password are displayed in the login form. 
- [templates/recipient.html]() contains the accompanying web interface for the recipient table that uses AJAX calls to perform CRUD operations. 
- [templates/vaccinator.html]() contains the accompanying web interface for the vaccinator table that uses AJAX calls to perform CRUD operations. 
- [templates/getWeather.html]() contains the submit form for the function 'get_weather' which links the server to a third party API to retrieve the current weather in any city/country. 
- [templates/weatherresult.html]() displays the searched weather result. 
- [templates/aimsir.html]() contains a barchart to display average weather from a csv file. 
- There are images in the style to try make the web pages look nice. I had tried to have a seperate style.css file but it kept producing errors and so the style is within the pages but the base.html file holds most script links. 


### Activate a virtual environment using the following commands on the command line:

- Make a virtual environment with a directory named venv.: <b> python -m venv venv</b>

- Run the virtual envirnoment: <b>.\venv\Scripts\activate.bat</b> on Windows or <b>source venv/bin/activate </b> on Mac/Linux 

 - See the packages: <b> pip freeze </b>

 - Save them to a file: <b> pip freeze > requirements.txt </b>

 - Load a file of packages: <b> pip install -r requirements.txt </b> 

 - Set the server environmental variable: <b>set FLASK_APP=app</b> on windows or <b>export FLASK_APP=app</b> on Mac. 

 - Run the server: <b> flask run </b>   This will start the application on http://127.0.0.1:5000/. Copy the link into your browser. Click the link to access the web interface.

  - To stop the server running: use <b> ctrl + c. </b>


## References:
- Andrew Beatty course material on moodle
- Andrew Beatty datarepresentation 2021 github 
- [open weather map](https://openweathermap.org/)- open weather map provides API keys to anyone who signs up by email. I used this API key to link to a third party API and retrieve weather data using get and post methods in python flask.  
- [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/)- The flask documentation goes through everything to do with flask. 
- [Tim Ruscica tutorial](https://www.techwithtim.net/tutorials/flask/)- Tim is the founder of Tech with Tim Inc and a programming course creator who has many tutorials and good youtube videos, I found this video on flask particularly helpful while working on this project. 
- [Python flask Website](https://csveda.com/python-flask-website-adding-routes-to-link-pages/)- "Adding Routes to Link Pages", Published June 7, 2020.
- [tutorialspoint.com](https://www.tutorialspoint.com/flask/index.htm), "Flask tutorial", - a very helpful tutorial that goes through everything step by step. 
- [w3schools](https://www.w3schools.com/) is a freemium educational website for learning coding online. Developed in 1998, its name is derived from the World Wide Web. W3Schools offers courses covering all aspects of web development. I found the following tutorials particularly helpful; 
    - [AJAX tutorial](https://www.w3schools.com/js/js_ajax_intro.asp) 
    - [JSON tutorial](https://www.w3schools.com/js/js_json_intro.asp) 
    - [bootstrap tutorial](https://www.w3schools.com/bootstrap5/bootstrap_get_started.php)
    - [CSS tutorial](https://www.w3schools.com/css/)
- [real python](https://realpython.com/) has  Python tutorials for developers of all skill levels, I found their [Flask tutorial](https://realpython.com/python-web-applications-with-flask-part-i/) very helpful. 


