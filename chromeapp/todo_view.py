from django.shortcuts import render
from .models import Todo
from django.http import JsonResponse
from django.db import IntegrityError
import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


def get_all_todo(request):
    todos = Todo.objects.filter(user=request.user.id)
    todos_list = [
        {
            'id': todo.id,
            'name': todo.name,
            'description': todo.description,
            'duedate': todo.duedate.strftime('%Y-%m-%d %H:%M:%S')
        }
        for todo in todos
    ]
    return JsonResponse({'todos_list':todos_list})

@csrf_exempt
def create_todo(request):
    data = json.loads(request.body)
    name = data['name']
    description = data['description']
    due_date = datetime.strptime(data['due_date'], '%d/%m/%Y %I:%M%p')
    todos = Todo(user=request.user,name=name,description=description,duedate=due_date)
    todos.save()
    return JsonResponse({
        "status":True,
        "msg":"sucessfully saved"
    })

@csrf_exempt
def edit_todo(request):

    data = json.loads(request.body)
    todo_id = data['id']
    name = data['name']
    description = data['description']
    due_date = datetime.strptime(data['due_date'], '%d/%m/%Y %I:%M%p')
    print(due_date)
    #edit_todo
    try:
        todos = Todo.objects.filter(user=request.user.id,id=todo_id)[0]
    except:
        return JsonResponse({
        "status":False,
        "msg":"todo_not_found"
    })

    todos.name = name
    todos.description = description
    todos.duedate = due_date
    todos.save()
    return JsonResponse({
        "status":True,
        "msg":"sucessfully_edited"
    })
@csrf_exempt
def delete_todo(request):
    Todo.objects.filter(user=request.user.id,id=request.GET["id"]).delete()
    return JsonResponse({
        "status":True,
        "msg":"sucessfully_deleted"
    })