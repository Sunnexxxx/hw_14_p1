from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Author, Tag
from .forms import PostForm


def all_posts(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    selected_tag = request.GET.get('tag')
    if selected_tag:
        posts = Post.objects.filter(tags__name=selected_tag)

    return render(request, 'blog/main.html', {'posts': posts, 'tags': tags, 'selected_tag': selected_tag})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/detail.html', {'post': post})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            author = request.POST.get('author')
            post = form.save(commit=False)
            author, created = Author.objects.get_or_create(name=author)
            post.author = author
            post.save()

            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'blog/create.html', {'form': form})


def delete_post(request, pk):
    product = Post.objects.get(pk=pk)
    product.delete()

    return redirect('post_list')


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/update.html', {'form': form})


