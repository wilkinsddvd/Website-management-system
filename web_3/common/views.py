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