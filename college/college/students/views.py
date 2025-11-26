from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student


# Create your views here.
def home(request):
    return render(request,'home.html')

def studhome(request):
    return render(request, 'students/studhome.html')


def studentslist(request):  
    students = Student.objects.all()
    return render(request, 'students/studentslist.html', {'students': students})
    
def studentsform(request):    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():            
            form.save()
            return redirect('studentslist')
    else:
        form = StudentForm()
    return render(request, 'students/studentsform.html', {'form': form})

