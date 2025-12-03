from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# Create your views here.
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))

def products(request):
    products=[
        {"name":"apple","price":100,"category":"fruits"},
        {"name":"mango","price":120,"category":"fruits"},
        {"name":"banana","price":100,"category":"fruits"}]
    return Response({"products":products},status=HTTP_200_OK)


@api_view(["POST"])
@permission_classes((AllowAny,))
def signup(request):
    form=UserCreationForm(data=request.data)
    if form.is_valid():
        user=form.save()
        return Response("Account created successfully",status=status.HTTP_201_CREATED)
    return Response(form.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username=request.data.get("username")
    password=request.data.get("password")
    if username is None or password is None:
        return Response({"error":"Please provide both username and password"},status=status.HTTP_400_BAD_REQUEST)
    user=authenticate(username=username,password=password)
    if not user:
        return Response({"error":"Invalid credentials"},status=status.HTTP_400_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token':token.key,'username':username},status=HTTP_200_OK)

