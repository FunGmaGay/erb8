from django.shortcuts import render, get_object_or_404
from listings.models import Listing
from django.core.paginator import Paginator

def listings(request):
    #return HttpResponse("<h1>Hello World!</h1>")
    listings = Listing.objects.filter(is_published = True)
    #Pagination
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page) 

    ##require the dictionary to pass the list to the template engine
    context = {
        ## all listings
        #  "listings":listings,
        ## only listings in a page
        "listings": paged_listings,
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    #return HttpResponse("<h1>about</h1>")
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {"listing":listing}
    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')



# Create your views here.
