from flask import Flask, request ,  jsonify
import pickle
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import RandomizedSearchCV

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, f1_score, balanced_accuracy_score, classification_report
from sklearn.metrics import auc, roc_curve, roc_auc_score

import json
app = Flask(__name__)

@app.route("/getResolutionAction" , methods=['POST'])
def getResolutionAction():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        print("RequestData:", data)
        naive_b_resoln1_model = pickle.load(open('./naive_b_resoln1_model.sav', 'rb'))
        naive_b_resoln2_model = pickle.load(open('./naive_b_resoln2_model.sav', 'rb'))
        naive_b_resoln3_model = pickle.load(open('./naive_b_resoln3_model.sav', 'rb'))
        naive_b_resoln4_model = pickle.load(open('./naive_b_resoln4_model.sav', 'rb'))
        d = processData(data)

        if ('resolutionAction1' == ''):
            result = naive_b_resoln1_model.predict(d)
        elif ('resolutionAction2' == ''):
            result = naive_b_resoln2_model.predict(d)
        elif ('resolutionAction3' == ''):
            result = naive_b_resoln3_model.predict(d)
        elif ('resolutionAction4' == ''):
            result = naive_b_resoln4_model.predict(d)
        return jsonify([{"action":str(result)}])
    else:
        return 'Content-Type not supported!'


def processData(data):
    caseLvl1 = data.get('caseLvl1', '')
    if (caseLvl1 == 'Trouble Management'):
        caseLvl1_cat =0
    else:
        caseLvl1_cat = 1

    caseLvl2 = data.get('caseLvl2', '')
    if (caseLvl2 == 'All Prod Intermittent'):
        caseLvl2_cat =0
    elif (caseLvl2 == 'All Prod No Svc'):
        caseLvl2_cat =1
    else:
        caseLvl2_cat =2

    caseLvl3 = data.get('caseLvl3', '')
    if (caseLvl3 == 'CPE No Sync'):
        caseLvl3_cat =0
    elif (caseLvl3 == 'Inside Issue'):
        caseLvl3_cat =1
    else:
        caseLvl2_cat =2

    caseLvl4 = data.get('caseLvl4', '')
    if (caseLvl4 == 'Dispatched to Premise'):
        caseLvl4_cat =0
    else:
        caseLvl4_cat =1

    caseLvl5 = data.get('caseLvl5', '')
    if (caseLvl5 == 'IS'):
        caseLvl5_cat =0
    else:
        caseLvl5_cat =1

    resolutionAction1 = data.get('resolutionAction1', '')
    if (resolutionAction1 == 'CheckNetworkOutage'):
        resolutionAction1_cat =0
    elif (resolutionAction1 == 'CheckRecentCaseThreshold'):
        resolutionAction1_cat =1
    else:
        resolutionAction1_cat =2


    resolutionAction1Res = data.get('resolutionAction1Result', '')
    if (resolutionAction1Res == 'No'):
        resolutionAction1Res_cat =0
    else:
        resolutionAction1Res_cat =1

    resolutionAction2 = data.get('resolutionAction2', '')
    if (resolutionAction2 == 'AddCaseToOutageCase'):
        resolutionAction2_cat =0
    elif (resolutionAction2 == 'CheckRecentCaseThreshold'):
        resolutionAction2_cat =1
    elif (resolutionAction2 == 'CloseCase'):
        resolutionAction2_cat =2
    elif (resolutionAction2 == 'DispatchTechnician'):
        resolutionAction2_cat =3
    elif (resolutionAction2 == 'EscalateCase'):
        resolutionAction2_cat =4
    else:
        resolutionAction2_cat =5

    resolutionAction2Result = data.get('resolutionAction2Result', '')
    if (resolutionAction2Result == 'End'):
        resolutionAction2Res_cat =0
    elif (resolutionAction2Result == 'No'):
        resolutionAction2Res_cat = 1
    else:
        resolutionAction2Res_cat =2

    resolutionAction3 = data.get('resolutionAction3', '')
    if (resolutionAction3 == 'CloseCase'):
        resolutionAction3_cat =0
    elif (resolutionAction3 == 'DispatchTechnician'):
        resolutionAction3_cat =1
    elif (resolutionAction3 == 'EscalateCase'):
        resolutionAction3_cat =2
    elif (resolutionAction3 == 'RestartModemAndCheck'):
        resolutionAction3_cat =3
    else:
        resolutionAction3_cat =4

    resolutionAction3Result = data.get('resolutionAction3Result', '')
    if (resolutionAction3Result == 'End'):
        resolutionAction3Res_cat =0
    elif (resolutionAction3Result == 'No'):
        resolutionAction3Res_cat = 1
    elif (resolutionAction3Result == 'Yes'):
        resolutionAction3Res_cat = 2
    else:
        resolutionAction3Res_cat =3

    resolutionAction4 = data.get('resolutionAction4', '')
    if (resolutionAction4 == 'CloseCase'):
        resolutionAction4_cat =0
    elif (resolutionAction4 == 'DispatchTechnician'):
        resolutionAction4_cat =1
    else:
        resolutionAction4_cat =2

    if ('resolutionAction1' ==''):
        return [[caseLvl1_cat,caseLvl2_cat,caseLvl3_cat,caseLvl4_cat,caseLvl5_cat]]
    elif ('resolutionAction2' == ''):
        return [[caseLvl1_cat, caseLvl2_cat, caseLvl3_cat, caseLvl4_cat, caseLvl5_cat,resolutionAction1_cat,resolutionAction1Res_cat]]
    elif ('resolutionAction3' == ''):
        return [[caseLvl1_cat, caseLvl2_cat, caseLvl3_cat, caseLvl4_cat, caseLvl5_cat,resolutionAction1_cat,resolutionAction1Res_cat,resolutionAction2_cat,resolutionAction2Res_cat]]
    else:
        return [[caseLvl1_cat, caseLvl2_cat, caseLvl3_cat, caseLvl4_cat, caseLvl5_cat,resolutionAction1_cat,resolutionAction1Res_cat,resolutionAction2_cat,resolutionAction2Res_cat,resolutionAction3_cat,resolutionAction3Res_cat]]


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')

