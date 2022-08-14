from django.shortcuts import render,get_object_or_404
from blog.models import Post
from datetime import datetime
from django.db.models import F

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(published_date__lte=datetime.today())
    context = {'posts':posts}
    Post.objects.filter(status=True).update(counted_views=F('counted_views')+1)
    return render(request, 'blog/blog-home.html',context)

def blog_single(request):
    posts = Post.objects.filter(published_date__lte=datetime.today())
    context = {'posts':posts}
    Post.objects.filter(status=True).update(counted_views=F('counted_views')+1)
    return render(request, 'blog/blog-single.html',context)

def test(request,pid):
    #post = Post.objects.get(id=pid)     
    post = get_object_or_404(Post,pk=pid)
    context = {'post':post}
    return render(request, 'test.html',context)
