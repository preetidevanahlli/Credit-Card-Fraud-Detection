from django.urls import path
from . import views

urlpatterns=[
    path('main.html', views.main, name="main"),
    path('login2.html', views.login2, name="login2"),
    path('choice.html',views.Classify, name="choice"),
    path('score.html',views.Classify2,name="score"),
    path('score1.html',views.Classify3,name="score1"),
    path('result1.html',views.Classify4,name="result1")
]