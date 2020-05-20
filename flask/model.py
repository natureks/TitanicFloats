import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import pickle

# def assign_cabin(cabin):
#     """
#     Function to create cabin levels based on first ltter of cabin
#     """
#     return(cabin[0])

# def clean_data(in_file, out_file):
#     """
#     Function to clean the original dataset and 
#     write the results to a new csv file
#     """
#     titanic_df = pd.read_csv(in_file)

#     # if the passanger didn't have a cabin put a Z in place
#     titanic_df['Cabin'].fillna('Z', inplace=True)

#     # create the cabin level column based on column
#     titanic_df['Cabin'] = titanic_df['Cabin'].apply(assign_cabin)

#     # drop columns that are unique per passenger or family
#     titanic_df.drop(columns=['Ticket', 'PassengerId', 'Name'], inplace=True)

#     # create age bins (equal sized bins)
#     bins = 11
#     titanic_df['Age'] = pd.qcut(titanic_df['Age'], q=bins)
#     titanic_df = pd.get_dummies(titanic_df, columns=['Age'])

#     # encode the categorical values
#     titanic_df = pd.get_dummies(titanic_df, columns=['Embarked', 'Cabin'])

#     # encode sex
#     encoder = LabelEncoder()
#     titanic_df['Sex'] = encoder.fit_transform(titanic_df['Sex'])

#     # write the file out for later usage
#     titanic_df.to_csv(out_file, index=False)

#     return(titanic_df)

def generate_ticket_data(ticket):
    """
    This function takes a dictionary of inputs and returns
    the np array formated for the model

    the input dictionary should look like this:
    ticket = {
        'ticket_class' : 3, # 1, 2, 3
        'sex' : 'm', # 'm', 'f'
        'siblings_spouse' : 0, # of siblings / spouses aboard the Titanic
        'parents_children' : 1, # - int - # of parents / children aboard the Titanic
        'fare' : 8000, # in 2020 USD
        'age' : 7, # integer
        'port' : 'S',   # C = Cherbourg, Q = Queenstown, S = Southampton
        'cabin' : 'Z' # A, B, C, D, E, F, G, T, Z
    }
    """

    if ticket['sex'] == 'f':
        sex = 0
    else:
        sex = 1

    fare = ticket['fare']

    ticket_list = [
        ticket['ticket_class'], 
        sex, 
        ticket['siblings_spouse'],
        ticket['parents_children'],
        fare
        ]

    if ticket['age'] < 12:
        ticket_list.append(1)
    else:
        ticket_list.append(0)

    if ticket['age'] >= 12 and ticket['age'] < 19:
        ticket_list.append(1)
    else:
        ticket_list.append(0)
    
    if ticket['age'] >= 19 and ticket['age'] < 22:
        ticket_list.append(1)
    else:
        ticket_list.append(0)
    
    if ticket['age'] >= 22 and ticket['age'] < 25:
        ticket_list.append(1)
    else:
        ticket_list.append(0)
    
    if ticket['age'] >= 25 and ticket['age'] < 28:
        ticket_list.append(1)
    else:
        ticket_list.append(0)

    if ticket['age'] >= 28 and ticket['age'] < 31:
        ticket_list.append(1)
    else:
        ticket_list.append(0)

    if ticket['age'] >= 31 and ticket['age'] < 34:
        ticket_list.append(1)
    else:
        ticket_list.append(0)

    if ticket['age'] >= 34 and ticket['age'] < 37:
        ticket_list.append(1)
    else:
        ticket_list.append(0)
    
    if ticket['age'] >= 37 and ticket['age'] < 43:
        ticket_list.append(1)
    else:
        ticket_list.append(0)

    if ticket['age'] >= 43 and ticket['age'] < 51:
        ticket_list.append(1)
    else:
        ticket_list.append(0)

    if ticket['age'] >= 41:
        ticket_list.append(1)
    else:
        ticket_list.append(0)

    if ticket['port'] == 'C':
        ticket_list.append(1)
    else:
        ticket_list.append(0)

    if ticket['port'] == 'Q':
        ticket_list.append(1)
    else:
        ticket_list.append(0)

    if ticket['port'] == 'S':
        ticket_list.append(1)
    else:
        ticket_list.append(0)
    
    if ticket['cabin'] == 'A':
        ticket_list.append(1)
    else:
        ticket_list.append(0)
    
    if ticket['cabin'] == 'B':
        ticket_list.append(1)
    else:
        ticket_list.append(0)
    
    if ticket['cabin'] == 'C':
        ticket_list.append(1)
    else:
        ticket_list.append(0)
    
    if ticket['cabin'] == 'D':
        ticket_list.append(1)
    else:
        ticket_list.append(0)
    
    if ticket['cabin'] == 'E':
        ticket_list.append(1)
    else:
        ticket_list.append(0)

    if ticket['cabin'] == 'F':
        ticket_list.append(1)
    else:
        ticket_list.append(0)

    if ticket['cabin'] == 'G':
        ticket_list.append(1)
    else:
        ticket_list.append(0)

    if ticket['cabin'] == 'T':
        ticket_list.append(1)
    else:
        ticket_list.append(0)

    if ticket['cabin'] == 'Z':
        ticket_list.append(1)
    else:
        ticket_list.append(0)

    return(np.array(ticket_list).reshape(1, -1))

def predict_results(model_file, ticket_data, ticket_num):
    """
    This function runs the ticket against the model
    and predicts survivability and probability of
    the result
    """
    model = pickle.load(open(model_file, "rb"))
    predicted = model.predict(ticket_data)
    prob = model.predict_proba(ticket_data).max().round(2)
    return([predicted[0], prob, ticket_num])


if __name__ == "__main__":

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
    
    ticket_data = generate_ticket_data(ticket)
    result = predict_results(model_file='clf_rfp.model', ticket_data=ticket_data, ticket_num =1)
    print(result)
    
