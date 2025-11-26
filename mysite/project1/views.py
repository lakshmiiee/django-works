from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login
from .forms import Registration
from .forms import BookModelForm,CustomerModelform
from .models import Books,Customer


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


def modelform(request):
    if request.method == 'POST':
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()

            books = Books.objects.all()   # get all records

            return render(request, 'modelformpost.html', {
                'message': 'Data saved to DB',
                'books': books
            })

    else:
        form = BookModelForm()

    return render(request, 'custform.html', {'form': form})

def cust(request):
    if request.method == 'POST':
        form = CustomerModelform(request.POST)
        if form.is_valid():
            form.save()
            cust=Customer.objects.all().order_by('name')
            filtered_customers = Customer.objects.filter(email__endswith='@example.com').order_by('name')

              

            return render(request, 'custformpost.html', {
                'message': 'Data saved to DB',
                'customer': cust,
                'filtered_customers': filtered_customers
            })

    else:
        form = CustomerModelform()

    return render(request, 'custform.html', {'form': form})

def custfiltered(request):
    if request.method == 'POST':
        form = CustomerModelform(request.POST)
        if form.is_valid():
            form.save()
           
            filtered_customers = Customer.objects.filter(email__endswith='@example.com').order_by('name')

              

            return render(request, 'custfiltered.html', {
                
                'filtered_customers': filtered_customers
            })

    else:
        form = CustomerModelform()

    
    return render(request,'custfiltered.html')
