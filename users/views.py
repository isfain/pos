from django.shortcuts import render

# Create your views here.

def usersTable(request):
    return render(request, 'user/users_table.html')
