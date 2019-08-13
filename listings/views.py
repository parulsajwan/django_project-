from django.shortcuts import render,get_object_or_404
from .models import Listing
from listings.choices import bedroom_choices ,price_choices ,state_choices
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator=Paginator(listings,2)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)

    context = {
        'listings': paged_listings

    }

    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)

    context={
        'listing':listing,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices
    }

    return render(request,'listings/listing.html',context)

def search(request):
    querryset_list=Listing.objects.order_by('-list_date')

#keyword
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            querryset_list=querryset_list.filter(description__icontains=keywords)
#city
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            querryset_list=querryset_list.filter(isexact=city)
#state
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            querryset_list=querryset_list.filter(isexact=state)
# price
        if 'price' in request.GET:
            price = request.GET['price']
            if price:
                querryset_list = querryset_list.filter(isexact=price)
# bedrooms
            if 'bedrooms' in request.GET:
                bedrooms = request.GET['bedrooms']
                if price:
                    querryset_list = querryset_list.filter(isexact=bedrooms)



    context={

        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings':querryset_list

    }
    return render(request,'listings/search.html',context)
