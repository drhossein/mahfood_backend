from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.


def login(request):
    """
    our custom login page.
    :param request:
    :return:
    """
    return render(request, "login_form.html")


def logout(request):
    pass


def index(request):
    pass