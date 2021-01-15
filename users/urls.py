from django.urls import path
from users.views import usersTable

urlpatterns = [
    path('', usersTable, name='User_Table' ),
]
