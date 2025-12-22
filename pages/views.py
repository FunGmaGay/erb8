from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'pages/index.html')

def about(request):
   #return HttpResponse("<h1>about</h1>")
   return render(request, 'pages/about.html')
