from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    students = ["Lakshmi", "Anu", "Rahul", "Vishnu"]
    return render(request, "home.html", {"students": students})


def result(request, name):
    # Fake student results — you can replace with a database later
    results = {
        "Lakshmi": "A+",
        "Anu": "B",
        "Rahul": "A",
        "Vishnu": "C+"
    }

    result = results.get(name, "No result found")
    
    return render(request, "result.html", {"name": name, "result": result})
