from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def login(request):
    """
    our custom login page.
    :param request:
    :return:
    """
    username, password = "", ""
    error = False
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return HttpResponseRedirect("/")
        error = True
    return render(request, "login_form.html",{
        "error": error
    })


def logout(request):
    pass


def index(request):
    pass