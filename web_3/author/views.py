from django.shortcuts import render, get_object_or_404

from.models import Author
from .models import AuthorProfile

# 11.16 压缩响应 更新
from django.views.decorators.gzip import gzip_page # 压缩响应

# 11.16 完善 author/views.py
# def articles_author(request,author_id):
#     ''' 查询指定作者的所有文章'''
#     # 查询得到作者对象
#     author = get_object_or_404(Author, pk=author_id)
#     # 查询作者的所有文章
#     articles = author.article_set.all()
#     return render(request, 'article/articles.html', {'author':author, 'articles':articles})
# @gzip_page # 压缩响应
# def articles_author(request, author_id):
#     ''' 查询指定作者的所有文章'''
#     author = get_object_or_404(Author, pk=author_id)
#     articles = author.article_set.all()
#     return render(request, 'article/articles.html', {'res_code':0, 'res_msg':'查询作者的所有文章',  'articles':articles})# 11.16 完善 author/views.py

from django.views.decorators.http import require_http_methods
@require_http_methods(['GET', 'POST'])
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

        # 创建并保存用户扩展资料对象 11.16
        authorprofile = AuthorProfile(author=author)
        authorprofile.save()

        # 跳转到登录页面
        return render(request, 'author/login.html', {'msg_code':0, 'msg_info':'账号注册成功，请登录。'})

@require_http_methods(['GET', 'POST'])
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
            # return render(request, 'author/index.html', {'msg_code':0, 'msg_info':'登录成功'}) 11.16 跳转到首页
            return render(request, 'author/index.html', {'msg_code':0, 'msg_info':'登录成功'})
        except :
            # 登录失败
            return render(request,  'author/login.html', {'msg_code':-1, 'msg_info':'用户名或密码错误,请重新登录'})