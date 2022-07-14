import numpy as np
import pandas as pd
from catboost import CatBoostClassifier,Pool
import plotly.graph_objects as go

# Global variable that stores trained model instance
MODEL = CatBoostClassifier().load_model('metabolic_syndrome2022-07-10')

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




