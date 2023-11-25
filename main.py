#import library
import uvicorn
from fastapi import FastAPI
from Models import Winner
import numpy as np
import pickle
import pandas as pd

#create the app object
app=FastAPI()
pickle_model=open("classifier.pkl","rb")
classifier = pickle.load(pickle_model)

#default route
@app.get('/')
def index():
    return{"message":"Welcome"}

#default route
@app.get('/api-demo')
def index():
    return{"message":"This is Winner prediction API"}

#Prediction Function, return the predicted result in JSON
@app.post('/predict')
def predict(data:Winner):
    #convert data obj to dictionary
    data=dict(data)
    Team_1_Encoded=data['Team_1_Encoded']
    Team_2_Encoded=data['Team_2_Encoded']

    label_mappings = {
    'India': 0, 'South Africa': 1, 'Netherlands': 2, 'Pakistan': 3,'New Zealand': 4, 'Sri Lanka': 5, 'Afghanistan': 6,'Australia':7,'Bangladesh':8,'England':9
    }

    predictions = classifier.predict([[label_mappings[Team_1_Encoded], label_mappings[Team_2_Encoded]]])

    if predictions[0] == 0:
        return "Winner: India"
    elif predictions[0] == 1:
        return "Winner: South Africa"
    elif predictions[0] == 2:
        return "Winner: Netherlands"
    elif predictions[0] == 3:
        return "Winner: Pakistan"
    elif predictions[0] == 4:
        return "Winner: New Zealand"
    elif predictions[0] == 5:
        return "Winner: Sri Lanka"
    elif predictions[0] == 6:
        return "Winner: Afghanistan"
    elif predictions[0] == 7:
        return "Winner: Australia"
    elif predictions[0] == 8:
        return "Winner: Bangladesh"
    else:
        return "Winner: England"
    

#Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    

#Command to run API server   
#python -m uvicorn main:app --reload
