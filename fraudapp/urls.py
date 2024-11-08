from django.contrib import admin
from django.urls import path
from .views import login2, choice, fraud , fraud1, result
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('login2.html', views.login2, name="login2"),
    path('choice.html', views.choice, name="choice"),
    path('fraud.html', views.fraud, name = "fraud"),
    path('fraud1.html', views.fraud1, name = "fraud1"),
    path('result.html', views.result, name = "result"),
   # path('predictor_2', views.predictor_2, name = 'predictor_2'),
  #  path('result_2', views.formInfo_2, name = 'result_2')
]