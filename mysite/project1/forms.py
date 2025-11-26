from django import forms 
from django.core.validators import validate_email
from django.core.validators import ValidationError
from .models import Books,Customer



def validation_email(value):
    if '@gmail' in value:
        raise ValidationError(
            'gmail is not allowed',
            params={'value':value},
        )

class Login(forms.Form):
    email=forms.EmailField(validators=[validate_email,validation_email])
    password=forms.CharField(min_length=6,widget=forms.PasswordInput)

class Registration(forms.Form):
    name=forms.CharField(min_length=5,max_length=50)
    email=forms.EmailField(validators=[validate_email,validation_email])
    password=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=20)


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

class CustomerModelform(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'