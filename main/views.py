from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def login_(request):
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
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                error = True
        error = True
    return render(request, "login_form.html",{
        "error": error
    })


def logout_(request):
    logout(request)
    return HttpResponseRedirect("/")


def index(request):
    return render(request, 'order.html')