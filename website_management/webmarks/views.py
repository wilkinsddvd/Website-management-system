# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Bookmark
from .forms import BookmarkForm

@login_required
def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    # bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'bookmarks/bookmark_list.html', {'bookmarks': bookmarks})

@login_required
def add_bookmark(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.user = request.user
            bookmark.save()
            return redirect('bookmark_list')
    else:
        form = BookmarkForm()
    return render(request, 'bookmarks/add_bookmark.html', {'form': form})

@login_required
def delete_bookmark(request, bookmark_id):
    bookmark = Bookmark.objects.get(id=bookmark_id, user=request.user)
    if bookmark:
        bookmark.delete()
    return redirect('user/bookmark_list')