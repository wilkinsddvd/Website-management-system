from django.shortcuts import render

def index(request):
    return render(request, 'index/index.html')

def login_page(request):
    return render(request, 'user/login.html')

