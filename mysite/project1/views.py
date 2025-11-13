from django.shortcuts import render
from django.http import HttpResponse

def greeting(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,"aboutus.html") 

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    return render(request,'contact.html')

def employee(request):
    employee=[
        {'name':'lakshmi','job':'IT','salary':25000,'status':'yes'},
        {'name':'anupama','job':'CA','salary':20000,'status':'no'},
        {'name':'divya','job':'Trainee','salary':15000,'status':'no'},
        {'name':'abhi','job':'IT','salary':35000,'status':'yes'}
    ]
    return render(request,'employee.html',{'employee':employee})

def students(request):
    students=[
        {'name':'badhra','grade':7,'passed':'yes'},
        {'name':'anu','grade':7,'passed':'no'},
        {'name':'arya','grade':7,'passed':'yes'},
        {'name':'devika','grade':7,'passed':'no'},

    ]
    return render(request,'students.html',{'students':students})

