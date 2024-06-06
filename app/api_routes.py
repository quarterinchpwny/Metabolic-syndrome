import pandas as pd
from flask import Blueprint, request
from services.model_utils import predict_hf


bp1 = Blueprint('main', __name__, url_prefix='/main')


def check_form_fields(form_data):
    required_fields = ['sex', 'Marital', 'Income', 'Race', 'WaistCirc', 'Age', 'BMI', 'Albuminuria', 'UrAlbCr', 'UricAcid', 'BloodGlucose', 'HDL', 'Triglycerides']
    
    missing_fields = [field for field in required_fields if field not in form_data]
    
    if missing_fields:
        print("The following fields are missing from the form:", missing_fields)
        return {'is_empty':True , 'missing_fields':missing_fields}
    else:
        print("All required fields are present in the form.")
        return True
    
@bp1.route('/api/make_prediction', methods=['POST'])

def make_prediction():
    
    checkFields = check_form_fields(request.form)
    if(checkFields['is_empty']):
        return {'missing_fields':checkFields['missing_fields'] , 'code':'422'}  
    
    
    # form_df:pd.DataFrame = pd.DataFrame(request.form, index=[0])
    
    # pred = predict_hf(form_df)
    # print(pred)
    # pred_class_1 = pred[0][0]
  


    # return {'pred':pred_class_1}

