import tra_functions as tralib
import model
from flask import Flask, redirect, jsonify, render_template, Response, request
from flask_cors import CORS
import socket
import os.path
import random

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

def read_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)

#################################################
# Flask Routes
#################################################

@app.route("/")
@app.route("/home")
@app.route("/index")
def welcome(): 
    return render_template("index.html")

@app.route("/redirect")
def redirect():
    return welcome()

@app.route("/get")
def get():
	hostname = socket.gethostname()    
	IPAddr = socket.gethostbyname(hostname)    
	print("Your Computer Name is:" + hostname)    
	print("Your Computer IP Address is:" + IPAddr)    
	ipDetails = f"Flask application IP Deails are:\nhostname='{hostname}', IPAddr='{IPAddr}'"

	return jsonify(ipDetails)

@app.route('/t/<string:page_name>/')
def render_template_html(page_name):
    return render_template('%s.html' % page_name)

@app.route("/get_crime_count")
def get_crime_count():
    crime_count = {
        'Agg Assault':'19150',
        'Auto Theft':'37653',
        'Homicide':'704',
        'Burglary':'51268',
        'Larceny':'138845',
        'Robbery':'18227'
    }
    return jsonify(crime_count)

@app.route("/get_map_data")
def get_map_data():
    crime_count = {
        'x':[1,2,3,4,5,6,7,8,9],
        'y':[1,2,3,4,5,6,7,8,9]
    }
    return jsonify(crime_count)

@app.route('/get_file', methods=['GET'])
def get_file():
    '''
    examples:
        http://localhost:5000/get_file?filename=csv\birth.csv
        http://localhost:5000/get_file?filename=static_html\hello.html
    '''
    args = request.args

    file_name = ""
    for k, v in args.items():
        # arg_str = f"{k}: {v}"
        file_name = v
        break

    content = read_file(file_name)
    content_type = "text/" + file_name.split('.')[1]
    return Response(content, mimetype=content_type)

@app.route('/getdf', methods=['GET'])
def get_df():
    args = request.args

    key = ""
    for k, v in args.items():
        key = v
        break

    return tralib.read_df_from_mongo_as_json(key)


@app.route('/api/get_passengers')
def get_passengers():
    '''
    examples:
        http://localhost:5000/api/get_passengers
    '''
    passenger = {1:("Mr","John","Smith","3","m","1","1","8","20","C","Z"), 2:("Mr","Todd","Rod","3","m","1","1","8","30","C","Z")}
    return jsonify(passenger)


@app.route('/api/test_prediction')
def test_prediction():
    ticket = {
        'ticket_class' : 3,
        'sex' : 'm',
        'siblings_spouse' : 0, # of siblings / spouses aboard the Titanic
        'parents_children' : 1, # - int - # of parents / children aboard the Titanic
        'fare' : 8000, # - int - Passenger fare input in USD range $
        'age' : 7,
        'port' : 'S',   # C = Cherbourg, Q = Queenstown, S = Southampton
        'cabin' : 'Z'
    }
    ticket_data = model.generate_ticket_data(ticket)
    result = model.predict_results(model_file='clf_rfp.model', ticket_data=ticket_data)

    rebuilt_result = {}
    rebuilt_result.update({"Survival": str(result[0])})
    rebuilt_result.update({"Probability": str(result[1])})
    rebuilt_result.update({"TicketNum": str(1)})
    
    return jsonify(rebuilt_result)


@app.route('/api/add_passenger/<title>/<fname>/<lname>/<ticket_class>/<sex>/<siblings_spouse>/<parents_children>/<fare>/<age>/<port>/<cabin>', methods=['GET', 'POST'])
def add_passenger(title, fname, lname, ticket_class, sex, siblings_spouse, parents_children, fare, age, port, cabin):
    '''
        Sample usage: # http://localhost:5000/api/add_passenger/Mr/John/Smith/3/m/1/1/8/20/C/Z
    '''

    ticket = {
        'ticket_class' : ticket_class,
        'sex' : sex,
        'siblings_spouse' : int(siblings_spouse), # of siblings / spouses aboard the Titanic
        'parents_children' : int(parents_children), # - int - # of parents / children aboard the Titanic
        'fare' : int(fare), # - int - Passenger fare input in USD range $
        'age' : int(age),
        'port' : port,   # C = Cherbourg, Q = Queenstown, S = Southampton
        'cabin' : cabin
    }

    ticket_data = model.generate_ticket_data(ticket)
    result = model.predict_results(model_file='clf_rfp.model', ticket_data=ticket_data)

    rebuilt_result = {}
    rebuilt_result.update({"Survival": str(result[0])})
    rebuilt_result.update({"Probability": str(result[1])})
    rebuilt_result.update({"TicketNum": str(random.randrange(1000))})
    
    return jsonify(rebuilt_result)

if __name__ == '__main__':
    app.run(debug=True)
