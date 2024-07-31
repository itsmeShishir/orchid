from django.http import HttpResponse

def Home(request):
    return HttpResponse(
        "Hello My name is shsihir")

def Blog(request):
    return HttpResponse(
        "Blog Page")