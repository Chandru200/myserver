from django.http import JsonResponse


class CustomAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.user.is_authenticated, "middleware")
        skip_authentication_middleware = [
            '/login_user', '/register', '/', '/logout', "/ProductivityMaster/PrivacyPolicy"]
        if not request.user.is_authenticated:
            if request.path not in skip_authentication_middleware:
                return JsonResponse({
                    "status": False,
                    "msg": "authentication_error"
                })

        response = self.get_response(request)
        return response
