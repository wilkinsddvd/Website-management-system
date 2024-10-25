from django.shortcuts import render

def runoob(request):
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    return render(request, "runoob.html", {"views_str": views_str})

# from django.shortcuts import render
# def runoob(request):
#     name ="菜鸟教程"
#     return render(request, "runoob.html", {"name": name})
# from django.shortcuts import render
#
# def runoob(request):
#     views_str = "<a href='https://www.baidu.com/'>点击跳转</a>"
#     return render(request, "runoob.html", {"views_str": views_str})

# from django.shortcuts import render
#
# def runoob(request):
#     views_dict = {"name":"菜鸟教程"}
#     return render(request, "runoob.html", {"views_dict": views_dict})
# from django.shortcuts import render
#
# def runoob(request):
#     views_list = ["菜鸟教程1","菜鸟教程2","菜鸟教程3"]
#     return render(request, "runoob.html", {"views_list": views_list})
# from django.shortcuts import render
#
# def runoob(request):
#   views_name = "菜鸟教程"
#   return  render(request,"runoob.html", {"name":views_name})
# from django.shortcuts import render,HttpResponse
#
#
# def runoob(request):
#     context = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'runoob.html', context)
# def hello(request):
#     return HttpResponse("Hello world ! ")