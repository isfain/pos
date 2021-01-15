from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
]
