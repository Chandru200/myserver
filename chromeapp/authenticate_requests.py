from django.http import JsonResponse
from .models import CustomUser

class CustomAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        from django.contrib.sessions.backends.db import SessionStore
        session_key = request.COOKIES.get('sessionid')
        session = SessionStore(session_key=session_key)
        session_data = session.load()
        email_id = session_data.get('email')
        skip_authentication_middleware = [
            '/getcsrf','/login_user', '/register', '/', '/logout', "/ProductivityMaster/PrivacyPolicy"]
        if request.path not in skip_authentication_middleware:
            if session_key is None or email_id is None:
                    return JsonResponse({
                        "status": False,
                        "msg": "authentication_error"
                    })
        if email_id:
            request.user  =  CustomUser.objects.get( email = email_id )
        response = self.get_response(request)
        return response
