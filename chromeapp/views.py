from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.http import JsonResponse
from django.db import IntegrityError
import json
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'chromeapp/index.html')


def privacypolicy(request):
    return render(request, 'chromeapp/privacypolicy.html')


@csrf_exempt
def login_user(request):
    print("came here1")
    data = json.loads(request.body)
    email = data['email']
    password = data['password']
    user = custom_authenticate(email=email, password=password)
    # user = authenticate(request, username="new", password="new")
    if user is not None:
        login(request, user)
        return JsonResponse({'msg': "logged in"})
    else:
        return JsonResponse({'msg': "username or password is incorrect"})


def logout_user(request):
    logout(request)
    return JsonResponse({'msg': "logged out sucessfully"})
    print("logout called")


@csrf_exempt
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
    print("came here")
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return None

    if user.check_password(password):
        return user

    return None
