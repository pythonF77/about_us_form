from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Post
def blog_list(request):
    posts = Post.objects.all()
    post_list = ""
    for post in posts:
        post_list += f"<li> {post}</li>"
    return HttpResponse(f"<ul>{post_list}</ul>")