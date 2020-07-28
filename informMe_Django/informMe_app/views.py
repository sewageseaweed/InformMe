from django.shortcuts import render
from informMe_app.models import Posts

# Create your views here.
# def inform_me(request):
#     return render(request, "home.html", {})

def posts_index(request):
    posts = Posts.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts_index.html', context)

def posts_detail(request, pk):
    posts = Posts.objects.get(pk=pk)
    context = {
        'posts': posts
    }
    return render(request, 'posts_detail.html', context)

