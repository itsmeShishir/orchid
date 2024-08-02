from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog
from category.models import Category

def HomePage(request):
    blogs = Blog.objects.all()
    category = Category.objects.all()
    context = {
        'blogs':blogs,
        'category':category
    }
    return render(request, "index.html",
                   {"context":context})