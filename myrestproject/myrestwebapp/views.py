from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees, diabetes_model, diabetes_prediction_model
from . serializers import employeesSerializers, diabetes_modelSerializers, diabetes_prediction_modelSerializers
from sklearn.externals import joblib
import numpy as np
import requests



class employeeList(APIView):

    def get(self,request):
        emp = employees.objects.all()
        serializer = employeesSerializers(emp,many=True)
        return Response(serializer.data)

    def post(self,request):
        print('POST Request \nData received at server')
        json_data = request.data
        print(json_data)

        emp = employees.objects.all()
        serializer = employeesSerializers(emp, many=True)
        return Response(serializer.data)

class JSON_Parser:
    '''
    This function takes json input and returns numpy array
    '''
    def parse(self, received_json_data):
        data = [[ \
            int(received_json_data['race']), int(received_json_data['gender']), int(received_json_data['age']), \
            float(received_json_data['weight']), \
            int(received_json_data['admission_type_id']), int(received_json_data['discharge_disposition_id']), \
            int(received_json_data['admission_source_id']), \
            int(received_json_data['time_in_hospital']), int(received_json_data['payer_code']), \
            int(received_json_data['medical_specialty']), int(received_json_data['num_lab_procedures']), \
            int(received_json_data['num_procedures']), int(received_json_data['num_medications']), \
            int(received_json_data['number_outpatient']), int(received_json_data['number_emergency']), \
            int(received_json_data['number_inpatient']), int(received_json_data['diag_1']), \
            int(received_json_data['diag_2']), \
            int(received_json_data['diag_3']), int(received_json_data['number_diagnoses']), \
            int(received_json_data['max_glu_serum']), int(received_json_data['A1Cresult']), \
            int(received_json_data['metformin']), \
            int(received_json_data['repaglinide']), int(received_json_data['nateglinide']), \
            int(received_json_data['chlorpropamide']), int(received_json_data['glimepiride']), \
            int(received_json_data['acetohexamide']), int(received_json_data['glipizide']), \
            int(received_json_data['glyburide']), \
            int(received_json_data['tolbutamide']), int(received_json_data['pioglitazone']), \
            int(received_json_data['rosiglitazone']), \
            int(received_json_data['acarbose']), int(received_json_data['miglitol']), \
            int(received_json_data['troglitazone']), int(received_json_data['tolazamide']), \
            int(received_json_data['examide']), \
            int(received_json_data['citoglipton']), int(received_json_data['insulin']), \
            int(received_json_data['glyburide_metformin']), int(received_json_data['glipizide_metformin']), \
            int(received_json_data['glimepiride_pioglitazone']), int(received_json_data['metformin_rosiglitazone']), \
            int(received_json_data['metformin_pioglitazone']), int(received_json_data['change']), \
            int(received_json_data['diabetesMed'])]]
        return data

class diabetes_data_machine_learning_predictor(APIView):

    def post(self,request):
        print('POST Request \nData received at server')
        received_json_data = request.data
        print(received_json_data)
        #load the trained model into memory
        saved_linear_regression_model = joblib.load(r'G:\IUPUI\Spring 18\ADC\Project\AI Models\linear_regression_model.pkl')
        # Example of input to model and it will predict output and return this to user
        # re_admitted = saved_linear_regression_model.predict([[2, 0, 0, 0.0, 6, 25, 1, 1, -1, 37, 41, 0, 1, 0, 0, 0, 124,\
        #                                                       -1, -1, 1, 0,0, -20, -20, -20, -20, -20, -20, -20, -20,-20,\
        #                                                       -20, -20, -20, -20, -20,-20, -20, -20, -20, -20, -20, -20,\
        #                                                       -20,-20, 0, 0]])

        re_admitted = saved_linear_regression_model.predict([[ \
            received_json_data['race'], received_json_data['gender'], received_json_data['age'],
            received_json_data['weight'], \
            received_json_data['admission_type_id'], received_json_data['discharge_disposition_id'],
            received_json_data['admission_source_id'], \
            received_json_data['time_in_hospital'], received_json_data['payer_code'],
            received_json_data['medical_specialty'], received_json_data['num_lab_procedures'], \
            received_json_data['num_procedures'], received_json_data['num_medications'],
            received_json_data['number_outpatient'], received_json_data['number_emergency'], \
            received_json_data['number_inpatient'], received_json_data['diag_1'], received_json_data['diag_2'],
            received_json_data['diag_3'], received_json_data['number_diagnoses'], \
            received_json_data['max_glu_serum'], received_json_data['A1Cresult'], received_json_data['metformin'],
            received_json_data['repaglinide'], received_json_data['nateglinide'], \
            received_json_data['chlorpropamide'], received_json_data['glimepiride'],
            received_json_data['acetohexamide'], received_json_data['glipizide'], received_json_data['glyburide'], \
            received_json_data['tolbutamide'], received_json_data['pioglitazone'], received_json_data['rosiglitazone'],
            received_json_data['acarbose'], received_json_data['miglitol'], \
            received_json_data['troglitazone'], received_json_data['tolazamide'], received_json_data['examide'],
            received_json_data['citoglipton'], received_json_data['insulin'], \
            received_json_data['glyburide_metformin'], received_json_data['glipizide_metformin'],
            received_json_data['glimepiride_pioglitazone'], received_json_data['metformin_rosiglitazone'], \
            received_json_data['metformin_pioglitazone'], received_json_data['change'],
            received_json_data['diabetesMed']]])

        print('Readmitted result',re_admitted)
        diabetes_prediction_model_obj = diabetes_prediction_model(re_admitted)
        serializer = diabetes_prediction_modelSerializers(diabetes_prediction_model_obj, many=False)
        return Response(serializer.data)

class diabetes_data_GaussianNB_predictor(APIView):

    # load the trained model into memory
    model = joblib.load(r'G:\IUPUI\Spring 18\ADC\Project\AI Models\Gausian_Naive_Bayes.pkl')

    def post(self,request):
        #print('POST Request \nData received at server')
        received_json_data = request.data
        #print(received_json_data)
        input_data = JSON_Parser().parse(received_json_data)
        re_admitted = self.model.predict(input_data)

        #print('Readmitted result',re_admitted)
        diabetes_prediction_model_obj = diabetes_prediction_model(re_admitted)
        serializer = diabetes_prediction_modelSerializers(diabetes_prediction_model_obj, many=False)
        return Response(serializer.data)

'''
class diabetes_data_DecisioTree_predictor(APIView):

    # load the trained model into memory
    model = joblib.load(r'G:\IUPUI\Spring 18\ADC\Project\AI Models\Decision_Tree.pkl')

    def post(self,request):
        print('POST Request \nData received at server')
        received_json_data = request.data
        print(received_json_data)

        re_admitted = self.model.predict([[ \
            int(received_json_data['race']), int(received_json_data['gender']), int(received_json_data['age']),\
            float(received_json_data['weight']), \
            int(received_json_data['admission_type_id']), int(received_json_data['discharge_disposition_id']),\
            int(received_json_data['admission_source_id']), \
            int(received_json_data['time_in_hospital']), int(received_json_data['payer_code']),\
            int(received_json_data['medical_specialty']), int(received_json_data['num_lab_procedures']), \
            int(received_json_data['num_procedures']), int(received_json_data['num_medications']),\
            int(received_json_data['number_outpatient']), int(received_json_data['number_emergency']), \
            int(received_json_data['number_inpatient']), int(received_json_data['diag_1']),\
            int(received_json_data['diag_2']),\
            int(received_json_data['diag_3']), int(received_json_data['number_diagnoses']), \
            int(received_json_data['max_glu_serum']), int(received_json_data['A1Cresult']),\
            int(received_json_data['metformin']),\
            int(received_json_data['repaglinide']), int(received_json_data['nateglinide']), \
            int(received_json_data['chlorpropamide']), int(received_json_data['glimepiride']),\
            int(received_json_data['acetohexamide']), int(received_json_data['glipizide']),\
            int(received_json_data['glyburide']), \
            int(received_json_data['tolbutamide']), int(received_json_data['pioglitazone']),\
            int(received_json_data['rosiglitazone']),\
            int(received_json_data['acarbose']), int(received_json_data['miglitol']), \
            int(received_json_data['troglitazone']), int(received_json_data['tolazamide']),\
            int(received_json_data['examide']),\
            int(received_json_data['citoglipton']), int(received_json_data['insulin']), \
            int(received_json_data['glyburide_metformin']), int(received_json_data['glipizide_metformin']),\
            int(received_json_data['glimepiride_pioglitazone']), int(received_json_data['metformin_rosiglitazone']), \
            int(received_json_data['metformin_pioglitazone']), int(received_json_data['change']),\
            int(received_json_data['diabetesMed'])]])

        print('Readmitted result',re_admitted)
        diabetes_prediction_model_obj = diabetes_prediction_model(re_admitted)
        serializer = diabetes_prediction_modelSerializers(diabetes_prediction_model_obj, many=False)
        return Response(serializer.data)
'''

class diabetes_data_LogisticsRegression_predictor(APIView):

    # load the trained model into memory
    model = joblib.load(r'G:\IUPUI\Spring 18\ADC\Project\AI Models\Logistic_Regression.pkl')
    #lda_model = joblib.load(r'G:\IUPUI\Spring 18\ADC\Project\AI Models\LDA.pkl')

    def post(self,request):
        #print('Logistics Regression')
        #print('POST Request \nData received at server')
        received_json_data = request.data
        #received_json_data = np.array(received_json_data).reshape(2,-1)
        #print(received_json_data)
        input_data = JSON_Parser().parse(received_json_data)

        re_admitted = self.model.predict(input_data)
        prob = self.model.predict_proba(input_data)
        #print (prob[0][re_admitted])
        if prob[0][re_admitted] < 0.60:
            #re_admitted = self.lda_model.predict(input_data)
            request = requests.post('http://localhost:8008/diabetes_LDA1/',data=received_json_data)
            print('Second Opinion')
        #print('Readmitted result',re_admitted)
        diabetes_prediction_model_obj = diabetes_prediction_model(re_admitted)
        serializer = diabetes_prediction_modelSerializers(diabetes_prediction_model_obj, many=False)
        return Response(serializer.data)


class diabetes_data_NeuralNetwork_predictor(APIView):

    # load the trained model into memory
    model = joblib.load(r'G:\IUPUI\Spring 18\ADC\Project\AI Models\Neural_Network.pkl')

    def post(self,request):
        #print('Neural Network')
        #print('POST Request \nData received at server')
        received_json_data = request.data
        #print(received_json_data)
        input_data = JSON_Parser().parse(received_json_data)
        re_admitted = self.model.predict(input_data)
        prob = self.model.predict_proba(input_data)
        # print (prob[0][re_admitted])
        if prob[0][re_admitted] < 0.60:
            # re_admitted = self.lda_model.predict(input_data)
            request = requests.post('http://localhost:9009/diabetes_GausianNB/', data=received_json_data)
            print('Second Opinion')

        print('Readmitted result',re_admitted)
        diabetes_prediction_model_obj = diabetes_prediction_model(re_admitted)
        serializer = diabetes_prediction_modelSerializers(diabetes_prediction_model_obj, many=False)
        return Response(serializer.data)

class diabetes_data_LDA_predictor(APIView):

    # load the trained model into memory
    model = joblib.load(r'G:\IUPUI\Spring 18\ADC\Project\AI Models\LDA.pkl')

    def post(self,request):
        #print('LDA Model')
        #print('POST Request \nData received at server')
        received_json_data = request.data
        #print(received_json_data)
        input_data = JSON_Parser().parse(received_json_data)
        re_admitted = self.model.predict(input_data)
        prob = self.model.predict_proba(input_data)
        #print (prob[0][re_admitted])
        if prob[0][re_admitted] < 0.60:
            #re_admitted = self.lda_model.predict(input_data)
            request = requests.post('http://localhost:7008/diabetes_LogisticsRegression1/',data=received_json_data)
            print('Second Opinion')


        print('Readmitted result',re_admitted)
        diabetes_prediction_model_obj = diabetes_prediction_model(re_admitted)
        serializer = diabetes_prediction_modelSerializers(diabetes_prediction_model_obj, many=False)
        return Response(serializer.data)


class diabetes_data_LogisticsRegression_predictor1(APIView):

    # load the trained model into memory
    model = joblib.load(r'G:\IUPUI\Spring 18\ADC\Project\AI Models\Logistic_Regression.pkl')
    #lda_model = joblib.load(r'G:\IUPUI\Spring 18\ADC\Project\AI Models\LDA.pkl')

    def post(self,request):
        #print('Logistics Regression')
        #print('POST Request \nData received at server')
        received_json_data = request.data
        #received_json_data = np.array(received_json_data).reshape(2,-1)
        #print(received_json_data)
        input_data = JSON_Parser().parse(received_json_data)
        re_admitted = self.model.predict(input_data)
        prob = self.model.predict_proba(input_data)
        #print (prob[0][re_admitted])
        if prob[0][re_admitted] < 0.60:
            #re_admitted = self.lda_model.predict(input_data)
            #request = requests.post('http://localhost:8008/diabetes_LDA1/',data=received_json_data)
            print('Second Opinion')
        #print('Readmitted result',re_admitted)
        diabetes_prediction_model_obj = diabetes_prediction_model(re_admitted)
        serializer = diabetes_prediction_modelSerializers(diabetes_prediction_model_obj, many=False)
        return Response(serializer.data)


class diabetes_data_NeuralNetwork_predictor1(APIView):

    # load the trained model into memory
    model = joblib.load(r'G:\IUPUI\Spring 18\ADC\Project\AI Models\Neural_Network.pkl')

    def post(self,request):
        #print('Neural Network')
        #print('POST Request \nData received at server')
        received_json_data = request.data
        #print(received_json_data)
        input_data = JSON_Parser().parse(received_json_data)
        re_admitted = self.model.predict(input_data)
        prob = self.model.predict_proba(input_data)
        # print (prob[0][re_admitted])
        if prob[0][re_admitted] < 0.60:
            # re_admitted = self.lda_model.predict(input_data)
            #request = requests.post('http://localhost:9009/diabetes_GausianNB/', data=received_json_data)
            print('Second Opinion')

        print('Readmitted result',re_admitted)
        diabetes_prediction_model_obj = diabetes_prediction_model(re_admitted)
        serializer = diabetes_prediction_modelSerializers(diabetes_prediction_model_obj, many=False)
        return Response(serializer.data)

class diabetes_data_LDA_predictor1(APIView):

    # load the trained model into memory
    model = joblib.load(r'G:\IUPUI\Spring 18\ADC\Project\AI Models\LDA.pkl')

    def post(self,request):
        #print('LDA Model')
        #print('POST Request \nData received at server')
        received_json_data = request.data
        #print(received_json_data)
        input_data = JSON_Parser().parse(received_json_data)
        re_admitted = self.model.predict(input_data)
        prob = self.model.predict_proba(input_data)
        #print (prob[0][re_admitted])
        if prob[0][re_admitted] < 0.60:
            #re_admitted = self.lda_model.predict(input_data)
            #request = requests.post('http://localhost:7008/diabetes_LogisticsRegression1/',data=received_json_data)
            print('Second Opinion')


        print('Readmitted result',re_admitted)
        diabetes_prediction_model_obj = diabetes_prediction_model(re_admitted)
        serializer = diabetes_prediction_modelSerializers(diabetes_prediction_model_obj, many=False)
        return Response(serializer.data)
