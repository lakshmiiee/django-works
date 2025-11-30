from django.shortcuts import render,redirect,get_object_or_404
from .forms import StudentForm
from .models import Student

# Create your views here.
def home(request):
    students = Student.objects.all()
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'students': students,
        'form': form,
    }
    return render(request, 'home.html', context)


def result_page(request, name):
    student = get_object_or_404(Student, name=name)
    return render(request, 'result.html', {'student': student})


