from django.shortcuts import render

from.models import Author

def author_register(request):
    # 作者注册
    # 判断请求方式
    if request.method == 'GET':
        return render(request, 'author/register.html',{})
    elif request.method == 'POST':
        # 获取前端页面传递的数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        realname = request.POST.get('realname')
        # 判断用户是否已经注册过
        author = Author.objects.filter(username=username)
        if len(author) >0:  # 存在该用户名
            return render(request, 'author/register.html', {'msg_code':0, 'msg_info':'该用户名已被注册'})
        # 创建作者对象
        author = Author(username=username, password=password, realname=realname)
        # 保存作者对象
        author.save()
        # 跳转到登录页面
        return render(request, 'author/login.html', {'msg_code':0, 'msg_info':'账号注册成功，请登录。'})

def author_login(request):
    # 作者登录
    # 判断请求方式
    if request.method == 'GET':
        return render(request, 'author/login.html',{})
    else:
        # 获取前端页面传递的数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 查询是否存在对应的用户
        try:
            author = Author.objects.get(username=username, password=password)
            # 登录成功，记录登录用户状态
            request.session['author'] = author
            # 跳转到首页
            return render(request, 'author/index.html', {'msg_code':0, 'msg_info':'登录成功'})
        except :
            # 登录失败
            return render(request,  'author/login.html', {'msg_code':-1, 'msg_info':'用户名或密码错误,请重新登录'})