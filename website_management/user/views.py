from django.shortcuts import render, get_object_or_404
from .models import User
from django.views.decorators.http import require_http_methods

# 11.22 新增

def views_function(request):
    # do something
    return render(request, 'user/index.html', {})

from django.shortcuts import render
from .models import User
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def author_register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html', {})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'user/register.html', {'msg_code': 0, 'msg_info': 'Passwords do not match'})

        author = User.objects.filter(username=username)
        if author.exists():
            return render(request, 'user/register.html', {'msg_code': 0, 'msg_info': 'Username already taken'})

        author = User(username=username, password=password)
        author.save()

        return render(request, 'user/login.html', {'msg_code': 0, 'msg_info': 'Account registered successfully, please login.'})

# @require_http_methods(['GET', 'POST'])
# def author_register(request):
#     # 作者注册
#     # 判断请求方式
#     if request.method == 'GET':
#         return render(request, 'user/register.html', {})
#     elif request.method == 'POST':
#         # 获取前端页面传递的数据
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         realname = request.POST.get('realname')
#         # 判断用户是否已经注册过
#         author = User.objects.filter(username=username)
#         if len(author) > 0:  # 存在该用户名
#             return render(request, 'user/register.html', {'msg_code': 0, 'msg_info': '该用户名已被注册'})
#         # 创建作者对象
#         author = User(username=username, password=password, realname=realname)
#         # 保存作者对象
#         author.save()
#
#         # 跳转到登录页面
#         return render(request, 'user/login.html', {'msg_code': 0, 'msg_info': '账号注册成功，请登录。'})

@require_http_methods(['GET', 'POST'])
def author_login(request):
    # 作者登录
    # 判断请求方式
    if request.method == 'GET':
        return render(request, 'user/login.html', {})
    else:
        # 获取前端页面传递的数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 查询是否存在对应的用户
        try:
            author = User.objects.get(username=username, password=password)
            # 登录成功，记录登录用户状态
            request.session['author'] = author
            # 跳转到首页
            return render(request, 'user/index.html', {'msg_code': 0, 'msg_info': '登录成功'})
        except:
            # 登录失败
            return render(request, 'user/login.html', {'msg_code': -1, 'msg_info': '用户名或密码错误,请重新登录'})

from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('/')

# from django.shortcuts import render, get _object_or_404
#
# from.models import User
#
# from django.views.decorators.http import require_http_methods
#
# # 11.22 新增
#
# def views_function(request):
#     # do something
#     return render(request,'user/index.html',{})
#
# @require_http_methods(['GET', 'POST'])
# def author_register(request):
#     # 作者注册
#     # 判断请求方式
#     if request.method == 'GET':
#         return render(request, 'user/register.html',{})
#     elif request.method == 'POST':
#         # 获取前端页面传递的数据
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         realname = request.POST.get('realname')
#         # 判断用户是否已经注册过
#         author = User.objects.filter(username=username)
#         if len(author) >0:  # 存在该用户名
#             return render(request, 'user/register.html', {'msg_code':0, 'msg_info':'该用户名已被注册'})
#         # 创建作者对象
#         author = User(username=username, password=password, realname=realname)
#         # 保存作者对象
#         author.save()
#
#     # 跳转到登录页面
#         return render(request, 'user/login.html', {'msg_code':0, 'msg_info':'账号注册成功，请登录。'})
#
# @require_http_methods(['GET', 'POST'])
# def author_login(request):
#     # 作者登录
#     # 判断请求方式
#     if request.method == 'GET':
#         return render(request, 'user/login.html',{})
#     else:
#         # 获取前端页面传递的数据
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # 查询是否存在对应的用户
#         try:
#             author = User.objects.get(username=username, password=password)
#             # 登录成功，记录登录用户状态
#             request.session['author'] = author
#             # 跳转到首页
#             # return render(request, 'author/index.html', {'msg_code':0, 'msg_info':'登录成功'}) 11.16 跳转到首页
#             return render(request, 'user/index.html', {'msg_code':0, 'msg_info':'登录成功'})
#         except :
#             # 登录失败
#             return render(request,  'user/login.html', {'msg_code':-1, 'msg_info':'用户名或密码错误,请重新登录'})
