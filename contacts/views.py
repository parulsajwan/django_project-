from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method=='POST':
        listing_id=request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if user has made inquiry already
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,"you are already make entry")
                return redirect('/listings/'+ listing_id)

        contact=Contact(listing=listing,listing_id=listing_id,name=name,
                        email=email,phone=phone,user_id=user_id)
        contact.save()

        send_mail(
            'property Listing Inquiry',
            "There has been inquired  for " + listing + '.sign into the admin panel fro more info ',
            'parulsajwan1999@gmail.com',
            [realtor_email,'stenzilouis19990@gmail.com'],
            fail_silently=False
        )
        messages.success(request,"your request has been submitted")
        return redirect ('/listings/'+ listing_id)
