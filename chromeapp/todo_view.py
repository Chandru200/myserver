from django.shortcuts import render
from .models import CustomUser
from django.http import JsonResponse
from django.db import IntegrityError
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt