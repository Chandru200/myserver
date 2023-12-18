from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("chromeapp.urls")),
    path('accounts/', include('allauth.urls')),
    path('socialaccount/', include('allauth.socialaccount.urls'))
]