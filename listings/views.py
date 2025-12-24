from django.shortcuts import render

def listings(request):
    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'listings/listings.html')

def listing(request, listing_id):
   #return HttpResponse("<h1>about</h1>")
   return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')



# Create your views here.
