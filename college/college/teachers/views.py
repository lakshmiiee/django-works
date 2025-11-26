from django.shortcuts import render,redirect
from .forms import TeachersForm
from .models import Teachers

def teachome(request):
    return render(request, 'teachers/teachome.html')


def teachlist(request):  
    teachers = Teachers.objects.all()
    return render(request, 'teachers/teachlist.html', {'teachers': teachers})
    
def teachform(request):    
    if request.method == 'POST':
        form = TeachersForm(request.POST)
        if form.is_valid():            
            form.save()
            return redirect('teachlist')
    else:
        form = TeachersForm()
    return render(request, 'teachers/teachform.html', {'form': form})


