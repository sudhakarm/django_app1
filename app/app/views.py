#from django.http import HttpResponse
from django.shortcuts import render
from core.forms import UserForm
from core.models import Users

def index(request):
    """ app views """
    return render(request, "list_users.html")