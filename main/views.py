from django.shortcuts import render, redirect
from .models import Post, Author
from .forms import PostForm


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/main.html', {'posts': posts})


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            author_name = request.POST.get('author_name')
            post = form.save(commit=False)
            author, created = Author.objects.get_or_create(name=author_name)
            post.author = author
            post.save()

            return redirect('all_posts')
    else:
        form = PostForm()

    return render(request, 'blog/create.html', {'form': form})


