from rest_framework import serializers
from . models import employees, diabetes_model, diabetes_prediction_model

class employeesSerializers(serializers.ModelSerializer):

    class Meta:
        model = employees
        fields = "__all__"
        #fields = {'firstName,lasttName'}


class diabetes_modelSerializers(serializers.ModelSerializer):

    class Meta:
        model = diabetes_model
        fields = "__all__"


class diabetes_prediction_modelSerializers(serializers.ModelSerializer):

    class Meta:
        model = diabetes_prediction_model
        fields = "__all__"

