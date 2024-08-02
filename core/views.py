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

def BlogPage(request):
    blog = Blog.objects.all()
    return render(request, "blog.html", 
                  {"blog":blog})


def CategoryPage(request):
    category = Category.objects.all()
    return render(request, "category.html", 
                  {"category":category})