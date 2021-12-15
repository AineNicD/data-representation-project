from flask import Flask, render_template, request, url_for, redirect, make_response, jsonify, flash, abort, session
from flask_mysqldb import MySQL
import requests
import json
import MySQLdb.cursors
import mysql.connector
from mysql.connector import cursor
import dbconfig 
from VaccinationDAO import recipientDao, vaccinatorDao


#Create the Flask app
app = Flask(__name__,
            static_url_path='',
            static_folder='templates')

# received an error needed a secret key so generated a random one 
app.secret_key = '02774c1c1fc7723ee19f4193'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'Vaccination'

mysql = MySQL(app)


# authorisation
@app.route('/')
def root():
    if not 'username' in session:
        return redirect(url_for('login'))
    return render_template('index.html')


# authorisation
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT username,pass FROM users WHERE username=%s", [username])
        user = cur.fetchone()
        if user:
            # session
            session['loggedin'] = True
            session['username'] = user['username']
            return render_template('index.html', username=username)
        
        else:
            flash('Invalid Username or Password !')
            return render_template('login.html')
    else:
        return render_template('login.html')



# Logout
@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')


#homepage
@app.route('/index')
def home():

    if not 'username' in session:
        return redirect(url_for('login'))

    return render_template('index.html')
    
    
#database page
@app.route('/database')
def database():

    if not 'username' in session:
        return redirect(url_for('login'))

    return render_template('database.html')
    
# recipient data on recipient page
@app.route('/recipientdata')
def recipientData():

    if not 'username' in session:
        return redirect(url_for('login'))

    return render_template('recipient.html')
    
    
# get all recipients
@app.route('/recipients')
def getAll():

    if not 'username' in session:
        abort(401)

    return jsonify(recipientDao.getAll())
    
# find recipient by id
@app.route('/recipients/<id>')
def findById(id):
    if not 'username' in session:
        abort(401)

    return jsonify(recipientDao.findById(id))

# create recipient
@app.route('/recipients', methods=['POST'])
def create():

    if not request.json:
        abort(400) 

    recipient={
        "id": request.json["id"],
        "firstname": request.json["firstname"],
        "surname":request.json["surname"],
        "vaccine":request.json["vaccine"]
    } 

    recipientAdd = recipientDao.create(recipient)
    
    return jsonify(recipientAdd)

# update recipient
@app.route('/recipients/<id>', methods =['PUT'])
def update(id):
    foundRecipient=recipientDao.findById(id)


    if foundRecipient == {}:
        return jsonify({}), 404

    if not request.json:
        abort(400)

    currentRecipient = foundRecipient

    if 'firstname' in request.json:
        currentRecipient['firstname'] = request.json['firstname']
    if 'surname' in request.json:
        currentRecipient['surname'] = request.json['surname']
    if 'vaccine' in request.json:
        currentRecipient['vaccine'] = request.json['vaccine']
    recipientDao.update(currentRecipient)

    return jsonify(currentRecipient)

# delete recipient 
@app.route('/recipients/<id>', methods =['DELETE'])
def delete(id):
    recipientDao.delete(id)
    return  jsonify( {'Done':True })


# vaccinator data 
@app.route('/vaccinatordata')
def vaccinatorData():

    if not 'username' in session:
        return redirect(url_for('login'))

    return render_template('vaccinator.html')

# get all vaccinators
@app.route('/vaccinators')
def getAllVaccinator():

    if not 'username' in session:
        abort(401)

    return jsonify(vaccinatorDao.getAllVaccinator())


# find vaccinator by id 
@app.route('/vaccinators/<reg_no>')
def findByReg(reg_no):
    if not 'username' in session:
        abort(401)

    return jsonify(vaccinatorDao.findByReg(reg_no))


# create vaccinator
@app.route('/vaccinators', methods=['POST'])
def createVaccinator():

    if not request.json:
        abort(400)  

    vaccinator = {
        "reg_no": request.json["reg_no"],
        "firstname": request.json["firstname"],
        "surname": request.json["surname"],
        "profession": request.json["profession"]
    }  

    vaccinatorAdd = vaccinatorDao.createVaccinator(vaccinator)

    return jsonify(vaccinatorAdd)

# update vaccinator 
@app.route('/vaccinators/<reg_no>', methods=['PUT'])
def updateVaccinator(reg_no):
    foundVaccinator = vaccinatorDao.findByReg(reg_no)

    if foundVaccinator == {}:
        return jsonify({}), 404

    if not request.json:
        abort(400)

    currentVaccinator = foundVaccinator

    if 'firstname' in request.json:
        currentVaccinator['firstname'] = request.json['firstname']
    if 'surname' in request.json:
        currentVaccinator['surname'] = request.json['surname']
    if 'profession' in request.json:
        currentVaccinator['profession'] = request.json['profession']

    vaccinatorDao.updateVaccinator(currentVaccinator)

    return jsonify(currentVaccinator)

# delete vaccinator
@app.route('/vaccinators/<reg_no>', methods=['DELETE'])
def deleteVaccinator(reg_no):
    vaccinatorDao.deleteVaccinator(reg_no)
    return jsonify({'Done': True})


# get weather through a third party api 
@app.route('/weather', methods=['GET', 'POST'])
def get_weather():
    
    if request.method == "POST":
        city = request.form['city']
        country = request.form['country']
        api_key = '69c044a9b954677a191157e56adeffa5'

        weather_url = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=metric')

        weather_data = weather_url.json()

        temp = round(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        return render_template("weatherresult.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city)
        
    if not 'username' in session:
        return redirect(url_for('login'))

    return render_template("getWeather.html")
    

if __name__ == '__main__':
    app.run(debug=True)