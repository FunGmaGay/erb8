#Function of views.py is to generate data from the database to show at the templates
from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
def index(request):
    #return HttpResponse("<h1>Hello World!</h1>")
    listings = Listing.objects.all()
    context = {"listings": listings} #to show all listings at index.html more easily
    #print(request, request.path)
    return render(request, 'pages/index.html', context)

def about(request):
    #return HttpResponse("<h1>about</h1>")
    print(request, request.path)
    return render(request, 'pages/about.html')
