from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login
from .forms import Registration

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

def form(request):
    if request.GET:
        username=request.GET.get('username')
        return render(request,'formdata.html',{
            'formdata':request.GET,
            'username':username
        })
    return render(request,"form.html")

def formpost(request):
    if request.method == 'POST':
     name = request.POST.get('name')
     return render(request,'formdatapost.html',{
         'formdatapost':request.POST,
         'name': name
     })
    return render(request,'formpost.html')

def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():  
            email = form.cleaned_data['email']
            return render(request, 'log_success.html', {'email': email})
        
    else:
        form = Login()  
    return render(request, 'login.html', {'form': form})

def reg(request):
    if request.method == 'POST':
        reg_form=Registration(request.POST)
        if reg_form.is_valid():
            name=reg_form.cleaned_data['name']
            return render(request,'reg_success.html',{'name':name })
    else:
        reg_form=Registration()

    return render(request,'reg.html',{'reg_form': reg_form})