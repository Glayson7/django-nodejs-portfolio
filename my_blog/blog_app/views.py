from django.shortcuts import render
from .models import Post


def homepage(request):
    posts = Post.objects.all().order_by("-published_date")
    return render(request, "homepage.html", {"posts": posts})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post_detail.html", {"post": post})
