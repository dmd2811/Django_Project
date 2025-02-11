from django.shortcuts import render
from .models import Post
# Create your views here.
def list_post(request):
    data = {'Posts': Post.objects.all().order_by("-date")}
    return render(request, "blog/blog.html", data)

def post(request, id):
    data = {'post': Post.objects.get(id = id)}
    return render(request, "blog/post.html", data)