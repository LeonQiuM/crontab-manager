from django.shortcuts import render
from django import views


# Create your views here.

def home(request):
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        pass

    elif request.method == "POST":
        pass

    else:
        pass


def login(request):
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        pass

    else:
        pass
