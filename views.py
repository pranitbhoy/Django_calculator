from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
def name(request):
    params={"name":"PRANIT ","city":"MUMBAI"}
    return render (request,"name.html",params)



def add(request):
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    result= val1+val2
    parameter={"ans":result}
    return render (request,"result.html",parameter)

def sub(request):
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    result = val1-val2
    para={"ans":result}
    return render (request,"result.html",para)
def div(request):
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    result = val1/val2
    para={"ans":result}
    return render (request,"result.html",para)

def mul(request):
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    result = val1*val2
    para={"ans":result}
    return render (request,"result.html",para)





