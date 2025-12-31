#Function of views.py is to generate data from the database to show at the templates
from django.shortcuts import render
#from django.http import HttpResponse
from listings.models import Listing
from doctors.models import Doctor
from listings.choices import district_choices, room_choices, rooms_choices
def index(request):
    #return HttpResponse("<h1>Hello World!</h1>")
    #listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {"listings": listings, #to show all listings at index.html more easily
               "district_choices": district_choices,
               "room_choices" : room_choices,
               "rooms_choices": rooms_choices,
    }
    #print(request, request.path)
    return render(request, 'pages/index.html', context)

def about(request):
    #return HttpResponse("<h1>about</h1>")
    doctors = Doctor.objects.order_by("-hire_date")[:3]
    mvp_doctors = Doctor.objects.all().filter(is_mvp=True).order_by('sort_order')
    context = {"doctors": doctors, "mvp_doctors": mvp_doctors}

    print(mvp_doctors)
    #print(request, request.path)
    return render(request, 'pages/about.html', context)
