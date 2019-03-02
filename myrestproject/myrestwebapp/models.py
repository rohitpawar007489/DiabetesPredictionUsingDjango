from django.db import models

# Create your models here.
class employees(models.Model):
    firstName=models.CharField(max_length=10)
    lastName=models.CharField(max_length=10)
    empid=models.IntegerField()

    def __str__(self):
        return self.firstName

class diabetes_model(models.Model):
    race = models.IntegerField()
    gender = models.IntegerField()
    age = models.IntegerField()
    weight = models.IntegerField()
    admission_type_id = models.IntegerField()
    discharge_disposition_id  = models.IntegerField()
    admission_source_id = models.IntegerField()
    time_in_hospital = models.IntegerField()
    payer_code = models.IntegerField()
    medical_specialty = models.IntegerField()
    num_lab_procedures = models.IntegerField()
    num_procedures = models.IntegerField()
    num_medications = models.IntegerField()
    number_outpatient = models.IntegerField()
    number_emergency = models.IntegerField()
    number_inpatient = models.IntegerField()
    diag_1 = models.IntegerField()
    diag_2 = models.IntegerField()
    diag_3 = models.IntegerField()
    number_diagnoses = models.IntegerField()
    max_glu_serum = models.IntegerField()
    A1Cresult = models.IntegerField()
    metformin = models.IntegerField()
    repaglinide = models.IntegerField()
    nateglinide = models.IntegerField()
    chlorpropamide = models.IntegerField()
    glimepiride = models.IntegerField()
    acetohexamide = models.IntegerField()
    glipizide = models.IntegerField()
    glyburide = models.IntegerField()
    tolbutamide = models.IntegerField()
    pioglitazone = models.IntegerField()
    rosiglitazone = models.IntegerField()
    acarbose = models.IntegerField()
    miglitol = models.IntegerField()
    troglitazone = models.IntegerField()
    tolazamide = models.IntegerField()
    examide = models.IntegerField()
    citoglipton = models.IntegerField()
    insulin = models.IntegerField()
    glyburide_metformin = models.IntegerField()
    glipizide_metformin = models.IntegerField()
    glimepiride_pioglitazone  = models.IntegerField()
    metformin_rosiglitazone = models.IntegerField()
    metformin_pioglitazone  = models.IntegerField()
    change = models.IntegerField()
    diabetesMed = models.IntegerField()


class diabetes_prediction_model(models.Model):
    re_admitted = models.IntegerField()

    def __init__(self, re_admitted):
        self.re_admitted = re_admitted
