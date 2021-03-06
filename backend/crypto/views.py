from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from .models import User
#from .Predict import Predict
from .FetchCryptoData import FetchCryptoData
import json

# Create your views here.
def index(request):
    data = FetchCryptoData()
    data.requestData("BTC","USD")
    print(data.data)
    return HttpResponse("Hello, world. You're at the crypto index.")

def getUsers(request, u_id):
    return HttpResponse("hi")

def getUserValues(request, u_id):
    return HttpResponse("hi")


@csrf_exempt
def submitSignup(request):
    # Parsing POST request
    post_data = request.body.decode()

    # Parse data from JSON string to dictionary
    data = json.loads(post_data)

    # Querying database to see if username is already there
    tempUser = User.objects.filter(user_name=data['username'])
   
    # if the
    if not tempUser:
        print(tempUser)
        return HttpResponse("Sorry, this email is already taken")
    else:
        u = User.objects.Create(user_name=data['username'],email=data['email'],password=data['password'])
        u.save()
        print(u)

# Function to handle user login.
#@ensure_csrf_cookie
@csrf_exempt
def submitLogin(request):
    # Parses response data from byte string to a string
    post_data = request.body.decode()
    
    # parses json string to dictionary
    data = json.loads(post_data)


    # if the user logs on with their email:
    if  data['email'] != None:
        # getting the user tuple from the database
        u = User.objects.filter(email=data['email'])
    elif data['username'] != None:
        u = User.objects.filter(user_name=data['username'])

    print(u)
    return HttpResponse("logged in")

