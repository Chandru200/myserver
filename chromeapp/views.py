from django.shortcuts import render
from django.contrib.auth import  logout
from .models import CustomUser
from django.http import JsonResponse
from django.db import IntegrityError
import json


def home(request):
    return render(request, 'chromeapp/index.html')


def privacypolicy(request):
    return render(request, 'chromeapp/privacypolicy.html')


def login_user(request):
    from django.contrib.sessions.models import Session
    data = json.loads(request.body)
    email = data['email']
    password = data['password']
    user = custom_authenticate(email=email, password=password)
    # user = authenticate(request, username="new", password="new")
    if user is not None:
        session_id = login(request, user).session_key
        response = JsonResponse({'msg': "logged in"})
        response.set_cookie('sessionid', session_id)
        return response
    else:
        return JsonResponse({'msg': "username or password is incorrect"})


def logout_user(request):
    logout(request)
    return JsonResponse({'msg': "logged out sucessfully"})


def register(request):
    try:
        data = json.loads(request.body)
        name = data['name']
        email = data['email']
        password = data['password']
        fromchrome = bool(data.get('fromchrome', False))

        user = CustomUser.objects.create_user(
            username=name, email=email, password=password, fromchrome=fromchrome)
        user.save()
        return JsonResponse({'email': email})

    except IntegrityError as e:
        return JsonResponse({'error': 'Email address is already in use'}, status=400)

    except Exception as e:
        return JsonResponse({'error': 'An error occurred'}, status=500)


def getuser(request):
    return JsonResponse({'name': "sss", 'authaa': request.user.is_authenticated})


def custom_authenticate(email, password):
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return None

    if user.check_password(password):
        return user

    return None

def login(request,user):
    request.session['email'] = user.email
    return request.session

def getcsrf(request):
    from django.middleware import csrf
    csrf_token = csrf.get_token(request)
    return JsonResponse({'csrf_token': csrf_token})
