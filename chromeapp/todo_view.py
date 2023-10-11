from .models import Todo, WebsiteMonitor
from django.http import JsonResponse
import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


def get_all_todo(request):
    response = {}
    todos = Todo.objects.filter(user=request.user.id)
    todos_list = [
        {
            'id': todo.id,
            'name': todo.name,
            'description': todo.description,
            'duedate': todo.duedate.strftime("%d/%m/%Y %I:%M%p")
        }
        for todo in todos
    ]
    response["todos_list"] = todos_list
    try:
        website_data = WebsiteMonitor.objects.filter(
            user=request.user.id, viewed_date=datetime.now().isoformat().split("T")[0])[0]
        response["view_time"] = website_data.view_time

    except Exception as e:
        print(e)
        response["view_time"] = {}
    return JsonResponse(response)


@csrf_exempt
def create_todo(request):
    data = json.loads(request.body)
    name = data['name']
    description = data['description']
    due_date = datetime.strptime(data['due_date'], '%d/%m/%Y %I:%M%p')
    todos = Todo(user=request.user, name=name,
                 description=description, duedate=due_date)
    todos.save()
    return JsonResponse({
        "status": True,
        "msg": "sucessfully saved",
        "id": todos.id
    })


@csrf_exempt
def edit_todo(request):

    data = json.loads(request.body)
    todo_id = data['id']
    name = data['name']
    description = data['description']
    due_date = datetime.strptime(data['due_date'], '%d/%m/%Y %I:%M%p')
    print(due_date)
    # edit_todo
    try:
        todos = Todo.objects.filter(user=request.user.id, id=todo_id)[0]
    except:
        return JsonResponse({
            "status": False,
            "msg": "todo_not_found"
        })

    todos.name = name
    todos.description = description
    todos.duedate = due_date
    todos.save()
    return JsonResponse({
        "status": True,
        "msg": "sucessfully_edited"
    })


@csrf_exempt
def delete_todo(request):
    Todo.objects.filter(user=request.user.id, id=request.GET["id"]).delete()
    return JsonResponse({
        "status": True,
        "msg": "sucessfully_deleted"
    })


@csrf_exempt
def delete_todo(request):
    Todo.objects.filter(user=request.user.id, id=request.GET["id"]).delete()
    return JsonResponse({
        "status": True,
        "msg": "sucessfully_deleted"
    })


@csrf_exempt
def set_view_time(request):
    data = json.loads(request.body)
    view_time = data['view_time']
    for date, perday_viewtime_data in view_time.items():
        try:
            website_data = WebsiteMonitor.objects.filter(
                user=request.user.id, viewed_date=date)[0]

            website_data.view_time = append_array_dicts(
                [website_data.view_time, perday_viewtime_data])
            website_data.viewed_date = date
            website_data.save()
        except:
            website_data = WebsiteMonitor(user=request.user, viewed_date=date,
                                          view_time=perday_viewtime_data)
            website_data.save()
    return JsonResponse({
        "status": True,
        "msg": "data_added"
    })


def get_view_time(request):
    try:
        date = convertStrToDateFromReq(request.GET["date"])
        website_data = WebsiteMonitor.objects.filter(
            user=request.user.id,  viewed_date=date)[0]
        return JsonResponse({
            "status": True,
            "view_time": website_data.view_time
        })
    except Exception as e:
        print(e, "error")
        return JsonResponse({
            "status": False,
            "view_time": {}
        })


def append_array_dicts(dict_array):
    new_dict = dict_array[0]
    for dict in range(1, len(dict_array)):
        for key, value in dict_array[dict].items():
            if key in new_dict:
                new_dict[key] = new_dict[key]+value
            else:
                new_dict[key] = value
    return new_dict


def convertStrToDateFromReq(date_str):
    date_str = date_str.strip("'")
    format = "%Y-%m-%d"
    date = datetime.strptime(date_str, format).date()
    return date
