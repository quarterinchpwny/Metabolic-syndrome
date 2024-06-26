import pandas as pd
from flask import Blueprint, request, jsonify
from services.model_utils import predict_hf


bp1 = Blueprint('api', __name__, url_prefix='/api')

def shape_response(code , message, data):
    response = {
            'code': code,
            'message': message,
            'data':data,
        }
    return response
def check_form_fields(form_data):
    required_fields = [
        'sex', 'Marital', 'Income', 'Race', 'WaistCirc', 'Age', 'BMI', 
        'Albuminuria', 'UrAlbCr', 'UricAcid', 'BloodGlucose', 'HDL', 
        'Triglycerides'
    ]
    
    missing_fields = [field for field in required_fields if field not in form_data]
    
    if missing_fields:
        return {'is_empty': True, 'missing_fields': missing_fields}
    return {'is_empty': False}

@bp1.route('/predict', methods=['POST'])

def predict():

    form_data = request.form
    check_fields = check_form_fields(form_data)

    if check_fields['is_empty']:
        data = {'missing_fields' : check_fields['missing_fields']}
        response = shape_response(422,'Invalid fields', data)
        return jsonify(response), 422

  
    # form_df = pd.DataFrame([form_data.to_dict()])
    # pred = predict_hf(form_df)
    # pred_class_1 = pred[0][0]
    # return jsonify({'pred': pred_class_1})

    return jsonify({'message': 'Prediction logic not implemented'}), 200

