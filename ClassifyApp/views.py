from django.shortcuts import render
from django.http import QueryDict

from joblib import load
classifier = load('./savedModels/classifier.joblib')

def main(request):
    return render(request,"main.html", {})

def login2(request):
    return render(request,"login2.html", {})

def Classify(request):
    return render(request, 'choice.html', {})

def Classify2(request):
    return render(request, 'score.html',{})

def Classify3(request):
    return render(request, 'score1.html',{})

def Classify4(request):
     id= request.GET.get('id')
     customerid=request.GET.get('customerid')
     month=request.GET.get('month')
     age= request.GET.get('age')
     ssn= request.GET.get('ssn')
     occupation=request.GET.get('occupation')
     annualincome=request.GET.get('annualincome')
     monthlyInhandSalary=request.GET.get('monthlyInhandSalary')
     noofbankaccounts=request.GET.get('noofbankaccounts')
     noofcreditcards=request.GET.get('noofcreditcards')
     interestRate= request.GET.get('interestRate')
     delayfromduedate= request.GET.get('delayfromduedate')
     noofdelayedpayments=request.GET.get('noofdelayedpayments')
     changedcreditlimit=request.GET.get('changedcreditlimit')
     noofcreditinquiries=request.GET.get('noofcreditinquiries')
     creditmix=request.GET.get('creditmix')
     outstandingdebt=request.GET.get('outstandingdebt')
     creditutilizationratio=request.GET.get('creditutilizationratio')
     credithistoryage=request.GET.get('credithistoryage')
     paymentofminamount=request.GET.get('paymentofminamount')
     totalemipermonth=request.GET.get('totalemipermonth')
     amountinvestedmonthly=request.GET.get('amountinvestedmonthly')
     paymentbehaviour=request.GET.get('paymentbehaviour')
     noofloans=request.GET.get('noofloans')
     monthlybalance=request.GET.get('monthlybalance')
     autoloan=request.GET.get('autoloan')
     creditbuilderloan=request.GET.get('creditbuilderloan')
     debtconsolidationloan=request.GET.get('debtconsolidationloan')
     homeequaityloan=request.GET.get('homeequaityloan')
     mortageloan=request.GET.get('mortageloan')
     notspecified=request.GET.get('notspecified')
     paydayloan=request.GET.get('paydayloan')
     personalloan=request.GET.get('personalloan')
     studentloan=request.GET.get('studentloan')

     
     y_pred = classifier.predict([[id,customerid,month,age,ssn,occupation,annualincome,monthlyInhandSalary,noofbankaccounts,noofcreditcards,interestRate,
       delayfromduedate,noofdelayedpayments,changedcreditlimit,noofcreditinquiries,creditmix,outstandingdebt,
       creditutilizationratio,credithistoryage,paymentofminamount,totalemipermonth,amountinvestedmonthly,
       paymentbehaviour,noofloans,monthlybalance,autoloan,creditbuilderloan,debtconsolidationloan,homeequaityloan,
       mortageloan,notspecified,paydayloan,personalloan,studentloan]])
    
     if y_pred[0]<1000:
        y_pred= "Good"
     elif 2000<y_pred[0]<5000:
        y_pred= "Standard"
     else:
        y_pred= "Good"
    
     return render(request,'result1.html',{'result1': y_pred})


