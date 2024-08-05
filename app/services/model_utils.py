import numpy as np
import pandas as pd
from catboost import CatBoostClassifier
import plotly.graph_objects as go
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'metabolic_syndrome2022-07-10')

# Global variable that stores trained model instance
MODEL = CatBoostClassifier().load_model(filename)

# Dictionary that converts frontend feature names to names understood by model
display_to_model = {'Age':'Age', 'sex':'Sex', 'Marital':'Marital', 'Income':'Income', 'Race':'Race', 'WaistCirc':'WaistCirc',
                    'BMI':'BMI','Albuminuria':'Albuminuria','UrAlbCr':'UrAlbCr' ,'UricAcid':'UricAcid',
                    'BloodGlucose':'BloodGlucose','HDL':'HDL', 'Triglycerides':'Triglycerides'}

def predict_hf(data:pd.DataFrame):

    # Make sure column names are correct
    data_predict = data.rename(display_to_model, axis=1)

    # Make sure columns are in the correct order
    data_predict = data_predict[MODEL.feature_names_]

    return MODEL.predict(data_predict)




