from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(),status=1)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request,id):
    posts = Post.objects.filter(published_date__lte=timezone.now(),status=1)
    post = get_object_or_404(posts,id=id)
    post.counted_views +=1
    post.save()
    next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()
    previous_post = Post.objects.filter(id__lt=post.id).order_by('id').last()
    context = {'post':post,'previous_post':previous_post,'next_post':next_post}
    return render(request, 'blog/blog-single.html', context)



