from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from main.models import Food


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


@login_required(login_url="/login")
def index(request):
    golabi = Food.objects.all()
    return render(request, 'order.html', {
        "foods": golabi
    })