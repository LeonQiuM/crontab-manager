from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from cmanage import models


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


@auth_required(auth_type='admin')
def home(request):
    """

    :param request:
    :return:
    """
    path1, path2 = "Home", '主页'
    if request.method == "GET":
        return render(request, 'home.html', locals())
    elif request.method == "POST":
        pass

    else:
        pass


@auth_required(auth_type='admin')
def hosts(request):
    """

    :param request:
    :return:
    """
    path1, path2, path3 = 'HOME', "主机", None
    if request.method == "GET":
        query_sets = models.Host.objects.all()
        return render(request, 'hosts.html', locals())

    elif request.method == "POST":
        pass

    else:
        pass


@auth_required(auth_type='admin')
def host_add(request):
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


@auth_required(auth_type='admin')
def host_del(request):
    """

    :param request:
    :return:
    """
    if request.method == "POST":
        host_id = request.POST.get("host_id", None)
        print(host_id)
        models.Host.objects.filter(host_id=host_id).delete()
        return HttpResponse("OK")


@auth_required(auth_type='admin')
def host_info(request, host_id):
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


@auth_required(auth_type='admin')
def hosts_task(request, host_id):
    """

    :param request:
    :return:
    """
    path1, path2, path3 = 'HOME', "主机", "主机任务"
    if request.method == "GET":
        host_obj = models.Host.objects.filter(host_id=host_id)
        tasks_obj = models.HostRuleStatus.objects.filter(host=host_obj)
        return render(request, 'host_tasks.html', locals())

    elif request.method == "POST":
        task_id = request.POST.get("task_id", None)
        option = request.POST.get("option", None)
        tasks_obj = models.HostRuleStatus.objects.filter(id=task_id)
        if option == "change":
            change_enable = request.POST.get("enable", None)
            if change_enable:
                if change_enable == "true":
                    tasks_obj.update(enable=False)
                elif change_enable == "false":
                    tasks_obj.update(enable=True)
        elif option == "del":
            tasks_obj.delete()
        return HttpResponse("OK")
    else:
        pass


@auth_required(auth_type='admin')
def host_groups(request):
    """

    :param request:
    :return:
    """
    path1, path2, path3 = 'HOME', "主机组", None
    if request.method == "GET":
        return render(request, 'host_groups.html', locals())

    elif request.method == "POST":
        pass

    else:
        pass


@auth_required(auth_type='admin')
def records(request):
    """

    :param request:
    :return:
    """
    path1, path2, path3 = 'HOME', "任务", None
    if request.method == "GET":
        return render(request, 'records.html', locals())

    elif request.method == "POST":
        pass

    else:
        pass
