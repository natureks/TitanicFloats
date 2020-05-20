# import tra_functions as tralib
import model
from flask import Flask, redirect, jsonify, render_template, Response, request
from flask_cors import CORS



#################################################
# Flask Setup
#################################################
app = Flask(__name__)


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

@app.route('/t/<string:page_name>/')
def render_template_html(page_name):
    return render_template('%s.html' % page_name)

passenger = {1:("Mr","John","Smith","3","m","1","1","8","20","C","Z"), 2:("Mr","Todd","Rod","3","m","1","1","8","30","C","Z")}


@app.route('/api/get_passengers')
def get_passengers():
    return jsonify(passenger)


@app.route('/api/add_passenger/<title>/<fname>/<lname>/<ticket_class>/<sex>/<siblings_spouse>/<parents_children>/<fare>/<age>/<port>/<cabin>', methods=['GET', 'POST'])
def add_passenger(title, fname, lname, ticket_class, sex, siblings_spouse, parents_children, fare, age, port, cabin):

    # ticket = {
    #     'ticket_class' : title,
    #     'sex' : sex,
    #     'siblings_spouse' : int(siblings_spouse), # of siblings / spouses aboard the Titanic
    #     'parents_children' : int(parents_children), # - int - # of parents / children aboard the Titanic
    #     'fare' : int(fare), # - int - Passenger fare input in USD range $
    #     'age' : int(age),
    #     'port' : port,   # C = Cherbourg, Q = Queenstown, S = Southampton
    #     'cabin' : cabin
    # }

    # ticket_data = model.generate_ticket_data(ticket)
    # result = model.predict_results(model_file='clf_rfp.model', ticket_data=ticket_data, ticket_num='1')
    result = [1, .57]
    result.append('1')
    return jsonify(result)


def predict_results(model_file, ticket_data):
    """
    This function runs the ticket against the model
    and predicts survivability and probability of
    the result
    """
    model = pickle.load(open(model_file, "rb"))
    predicted = model.predict(ticket_data)
    prob = model.predict_proba(ticket_data).max().round(2)
    return([predicted[0], prob])


if __name__ == '__main__':
    app.run(debug=True)


# http://localhost:5000/api/add_passenger/Mr/John/Smith/3/m/1/1/8/20/C/Z