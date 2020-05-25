# TitanicFloats
Machine Learning For Titanic Voyage

| First Name | Git-Username   | Last Name |
|------------|----------------|-----------|
| Kevin      | balhoffk       | Balhoff   |
| Jackie     | JKx2020        | Kamprath  |
| Kannan     | natureks       | Sekkappan |
| Georgia    | geleigh        | Leigh     |
| Ethan      | ethanemartin95 | Martin    |
| Shane      | hobbyhack      | Gary      |

## Links
Url of Github Repo of your Project:
	https://github.com/natureks/TitanicFloats

Website I (AWS S3):
	http://titanic-floats-the-ml-kings.s3-website-us-east-1.amazonaws.com/

Website II (Github)
	https://natureks.github.io/TitanicFloats/

Our API Server is:
	https://young-beach-08773.herokuapp.com/

Detailed Presentation:
	https://docs.google.com/document/d/1s7mY0sicZ6n-Qa2ILyjBlaZWULDR-BqLOlj37mQ_7es/edit


## Overview
For our project, out team is planning on utilizing data on the passengers of the Titanic. We will use the skills we have learned to help develop a model which predicts the liklihood of survival for passengers based on some of their personal information.

Our dataset currently includes information such as age, sex, cabin location, and fare (price paid for ticket). We intend to explore the relationship among these variables and the survival rate of the passengers.

Once we have developed our model, our team intends to create a webpage where users can enter their own information and find out what their liklihood of survival would be based on their demographics and the tickets they purchase.

We are also planning on databasing entries for people who add entries to the site, to see what the survival rate is for hypothetical additional passengers today!


## Key Programs:
<h3>ML Notebook</h3>
<pre>
	data/titanic1.ipynb
</pre>

<h3>Flask Application</h3>
<pre>
	flask/manage.py
</pre>

<h3>Website</h3>
<pre>
	index.html
</pre>

## API Calls
<h3>Add Passenger</h3>
<pre>
		API: https://young-beach-08773.herokuapp.com/api/add_passenger/Mr/John/Smith/3/f/1/1/8/20/C/Z
		Output: {"Probability":"0.52","Survival":"0","TicketNum":"48"}
</pre>
<h3>Get List Of Passengers</h3>
<pre>
	Get List Of Passengers
		API: https://young-beach-08773.herokuapp.com/api/get_passengers
		Output: {"47":[47,"Mr","John","Smith","1","f",1,1,8,20,"C","Z",0.7,1],"48":[48,"Mr","John","Smith","3","f",1,1,8,20,"C","Z",0.52,0]}
</pre>

## Project
<h3>Architectural Diagram</h3>
<img src = "/images/TitanicFloatsArchitecture.png" width = "500" height = "250">
