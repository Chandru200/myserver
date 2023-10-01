from django.http import JsonResponse

class CustomAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.user.is_authenticated, "middleware")
        if not request.user.is_authenticated:
            if request.path != '/login_user' and request.path != '/register' and request.path != '/':
                return JsonResponse({
                    "status": False,
                    "msg": "Login to access the data"
                })
        
        response = self.get_response(request)
        return response
