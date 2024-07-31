from django.shortcuts import render
from .models import Blog

# Create your views here.
def BlogPage(request):
    blogs = Blog.objects.all()
    return render(request, "index.html",
                   {"blogs":blogs})

