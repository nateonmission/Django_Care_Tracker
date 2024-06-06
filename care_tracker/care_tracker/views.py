from django.shortcuts import render, HttpResponse


def homepage(request):
#    return HttpResponse("<h1>Hello, World!</h1>")
    return render(request, 'home.html')

def about(request):
#    return HttpResponse("<H1>ABOUT</h1>")
    return render(request, 'about.html')