from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    all_post = Post.objects.all()
    '''for post in all_post:
        print(post)
        print(post.title)
        print(post.description)'''
    return render(request, 'index.html', {
        'all_post_list': all_post
    })

def student(request):
    return render(request, 'students.html')

def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'post_list.html', {
        'post_list': post_list
    })

def single_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    print(post)
    return render(request, 'single_post.html', {
        'post': post
    })
