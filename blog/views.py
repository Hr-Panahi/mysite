from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post,Comment
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages

# Create your views here.

def blog_view(request,**kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now(),status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request,id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'comment submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, "Your comment didn't submit.")

    posts = Post.objects.filter(published_date__lte=timezone.now(),status=1)
    post = get_object_or_404(posts,id=id)
    if not post.login_require:
        comments = Comment.objects.filter(posts=post.id,approved=True)
        post.counted_views +=1
        post.save()
        next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()
        previous_post = Post.objects.filter(id__lt=post.id).order_by('id').last()
        form = CommentForm()
        context = {'post':post,'previous_post':previous_post,'next_post':next_post, 'comments':comments, 'form':form}
        return render(request, 'blog/blog-single.html', context)
    else:
        return redirect('/accounts/login')
 
def test(request):
    return render(request,'test.html')

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(),status=1)

    if request.method == 'GET':
        if s := request.GET.get('s'): #---> using python walrus operator here 
            posts = posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)



