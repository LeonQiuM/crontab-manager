from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login,logout


# Create your views here.
def auth_required(auth_type):
    def wapper(func):
        def inner(request, *args, **kwargs):
            if auth_type == 'admin':
                ck = request.COOKIES.get("login")  # 获取当前登录的用户
                if request.user.is_authenticated() and ck:
                    return func(request, *args, **kwargs)
                else:
                    return redirect("/web/login/")

        return inner

    return wapper


@auth_required(auth_type='admin')
def home(request):
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        pass

    else:
        pass


def my_login(request):
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                response = redirect("/web/home/")
                response.set_cookie("login", username, max_age=1800)
                return response
            else:
                return redirect('/web/login/')
        else:
            return redirect('/web/login/')
    else:
        pass


def my_logout(request):
    # 注销
    if request.method == 'GET':
        logout(request)
        return redirect('/web/login/')