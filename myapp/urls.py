from django.urls import path
from .views import Classify4, index, result2
from . import views

urlpatterns=[
    path('result1.html', views.Classify4, name="result1"),
    path('index.html', views.index, name="index"),
    path('result2.html', views.result2, name="result2"),
    path('update.html', views.update, name="update"),


]
    