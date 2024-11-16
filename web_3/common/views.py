from django.db import models
from django.shortcuts import render,HttpResponse,Http404,loader

def page404error(request, exception):
    return render(request, 'html/pageerror.html',{
        'status_code': 404,
        'message': '抱歉客官，您要访问的资源还没上线呢'
    },
    status=404)

def page400error(request,exception):
    return render(request, 'html/pageerror.html',{
        'status_code': 400,
        'message': '客官，您的请求出问题了'
    },
    status=400)

def page403error(request,exception):
    return render(request, 'html/pageerror.html',{
        'status_code': 403,
        'message': '客官，您的权限不够呢'
    },
    status=403)



def page500error(request):
    return render(request, 'html/pageerror.html', {
        'status_code': 500,
        'message': '请稍等，系统正在升级中'
    }, status=500)


def index(request):
    # 使用加载器加载网页文件数据
    t = loader.get_template('html/index.html')
    c = {'message':'尊敬的用户您好，欢迎访问博客'}
    return render(request, 'html/index.html', {'message': '欢迎来到首页'})

# 11.16 更新 基本视图函数的定义
# 11.16 第一次修改公共模块中的视图模块
# def index(request):
#
#     return render(request, 'html/index.html',{'message':'欢迎来到首页'})

# 11.16 修改，本来全部都是注释掉的
# from django.db import models
# from django.shortcuts import render
#
# def page400error(request, **kwargs):
#     return render(request, 'pageerror.html',
#                   {'status_code':'400','message':'客官，您的请求出问题了'})
#
# def page403error(request, **kwargs):
#     return render(request, 'pageerror.html',
#                   {'status_code':'403','message':'客官，您的权限不够呢'})
#
# def page404error(request, **kwargs):
#     return render(request, 'pageerror.html',
#                   {'status_code':'404','message':'抱歉客官，您要访问的资源还没上线呢'})
#
# def page500error(request, **kwargs):
#     return render(request, 'pageerror.html',
#                   {'status_code':'500','message':'请稍等，系统正在升级中'})