"""myrestproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from myrestwebapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', views.employeeList.as_view()),
    path('diabetes/', views.diabetes_data_machine_learning_predictor.as_view()),
    path('diabetes_GausianNB/', views.diabetes_data_GaussianNB_predictor.as_view()),
    #path('diabetes_DecisionTree/', views.diabetes_data_DecisioTree_predictor.as_view()),
    path('diabetes_LogisticsRegression/', views.diabetes_data_LogisticsRegression_predictor.as_view()),
    path('diabetes_NeuralNetwork/', views.diabetes_data_NeuralNetwork_predictor.as_view()),
    path('diabetes_LDA/', views.diabetes_data_LDA_predictor.as_view()),
    path('diabetes_LogisticsRegression1/', views.diabetes_data_LogisticsRegression_predictor1.as_view()),
    path('diabetes_NeuralNetwork1/', views.diabetes_data_NeuralNetwork_predictor1.as_view()),
    path('diabetes_LDA1/', views.diabetes_data_LDA_predictor1.as_view()),
]
