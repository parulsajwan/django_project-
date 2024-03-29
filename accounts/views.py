from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # chk if pass match or not
        if password == password2:
            # chk username
            if User.objects.filter(username=username).exists():
                messages.error(request, "username already exists")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "email already exists")
                    return redirect("register")
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request,":you are now registered")
                    return redirect('login')
        else:
            messages.error(request, "password does match ")
            return redirect("register")
    else:
        return render(request, "accounts/register.html")

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"you are logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "invalid ")
            return redirect('login')
    else:
        return render(request,"accounts/login.html")

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"you are now logged out ")
        return redirect("logout")

def dashboard(request):
    user_contacts =Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'contacts': user_contacts
    }
    return render( request,"accounts/dashboard.html")

