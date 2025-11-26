from django import forms
from .models import Teachers

class TeachersForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ['name', 'department']  # add fields you want in form


