from django.contrib import admin
from . models import employees, diabetes_model, diabetes_prediction_model

# Register your models here.
admin.site.register(employees)
admin.site.register(diabetes_model)
admin.site.register(diabetes_prediction_model)
