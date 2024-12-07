from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Website

@require_http_methods(['GET', 'POST'])
def add_website(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        description = request.POST.get('description', '')
        Website.objects.create(url=url, description=description)
        return redirect('website:list')
    return render(request, 'website/add_website.html')

@require_http_methods(['POST'])
def delete_website(request, web_id):
    website = get_object_or_404(Website, web_id=web_id)
    website.delete()
    return redirect('website:list')

def list_websites(request):
    websites = Website.objects.all()
    return render(request, 'website/list_websites.html', {'websites': websites})

@require_http_methods(['GET', 'POST'])
def edit_website(request, web_id):
    website = get_object_or_404(Website, web_id=web_id)
    if request.method == 'POST':
        url = request.POST.get('url')
        description = request.POST.get('description', '')

        if not url:
            return render(request, 'website/edit_website.html', {'website': website, 'error': 'URL cannot be empty'})

        website.url = url
        website.description = description
        website.save()
        return redirect('website:list')
    return render(request, 'website/edit_website.html', {'website': website})




# 无法用按钮
# @require_http_methods(['GET', 'POST'])
# def edit_website(request, web_id):
#     website = get_object_or_404(Website, web_id=web_id)
#     if request.method == 'POST':
#         website.url = request.POST.get('url')
#         website.description = request.POST.get('description', '')
#         website.save()
#         return redirect('website:list')
#     return render(request, 'website/edit_website.html', {'website': website})

# @require_http_methods(['GET', 'POST'])
# def edit_website(request, web_id):
#     website = get_object_or_404(Website, web_id=web_id)
#     if request.method == 'POST':
#         website.url = request.POST.get('url')
#         website.description = request.POST.get('description', '')
#         website.save()
#         return redirect('website:list')
#     return render(request, 'website/edit_website.html', {'website': website})@require_http_methods(['GET', 'POST'])

'''delete_website 备份'''
# @require_http_methods(['POST'])
# def delete_website(request, website_id):
#     website = get_object_or_404(Website, id=website_id)
#     website.delete()
#     return redirect('website:list')

