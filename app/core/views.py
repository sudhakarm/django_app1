from django.shortcuts import render
from .forms import UserForm
from .models import Users

def add_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, "add_user.html", context)

def list_users(request):
    users = Users.objects.all()
    context = {
        'users': users
    }
    return render(request, "list_users.html", context)
