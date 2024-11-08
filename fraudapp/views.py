from django.http import HttpResponse
from django.shortcuts import render
from django.http import QueryDict

from joblib import load
clf_XGBClassifier = load('./savedModels/clf_XGBClassifier.joblib')

def main(request):
    return render(request,"main.html", {})

def login2(request):
    return render(request,"login2.html", {})

def choice(request):
    return render(request,"choice.html", {})

def fraud(request):
    return render(request,"fraud.html", {})

def fraud1(request):
    username = request.GET.get('username')
    print(username)
    return render(request, "fraud1.html", {'fraud1': username})

def result(request):
    transaction = request.GET.get('transaction')
    time = request.GET.get('time')
    amount = request.GET.get('amount')
    Class = request.GET.get('Class')
    Class_pred = clf_XGBClassifier.predict([[Class,transaction, time, amount, ]])
    
    if Class_pred[0] == 0:
        Class_pred = 'Legitimate'
    elif Class_pred[0]== 1:
        Class_pred = 'Fraud'
    else:
        print("Wrong Data Inserted")
    return render(request,"result.html",{'result': Class_pred})


'''def formInfo(request):
    username = request.GET('username')
    return render(request, 'result.html',{'name':username})

def predictor_2(request):
    return render(request,'fraud1.html')

def formInfo_2(request):
    transaction = request.GET['transaction']
    time = request.GET['time']
    amount = request.GET['amount']
    Class = request.GET['Class']
    Class_pred = xgb_classifier.predict([[transaction, time, amount, Class]])
    if Class_pred[3] == 0:
        Class_pred = 'Legitmate'
    elif Class_pred[3] == 1:
        Class_pred = 'Fraud'
    
    return render(request,'result_2.html',{'result_2': Class_pred})'''