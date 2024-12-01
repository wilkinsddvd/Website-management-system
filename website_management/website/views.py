from django.shortcuts import render, redirect, get_object_or_404
from .models import Website
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def add_website(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        description = request.POST.get('description', '')
        Website.objects.create(url=url, description=description)
        return redirect('website:list')
    return render(request, 'website/add_website.html')

@require_http_methods(['POST'])
def delete_website(request, website_id):
    website = get_object_or_404(Website, id=website_id)
    website.delete()
    return redirect('website:list')

def list_websites(request):
    websites = Website.objects.all()
    return render(request, 'website/list_websites.html', {'websites': websites})