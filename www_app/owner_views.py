from django.shortcuts import render, redirect
from .forms import PropertyOwnerLoginForm, PropertyOwnerForm, PropertyForm
from .models import PropertyOwner
from django.contrib import messages

def owner_register(request):
    if request.method == 'POST':
        form = PropertyOwnerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('owner_login')
    else:
        form = PropertyOwnerForm()
    return render(request, 'owner/register.html', {'form': form})

def owner_login(request):
    if request.method == 'POST':
        form = PropertyOwnerLoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')
            user_list = PropertyOwner.objects.filter(phone=phone, password=password)
            size = len(user_list)
            if size>0:
                request.session["session_key"] = phone
                return redirect('home')
            else:
                messages.error(request, 'Wrong Credentials')
                return render(request, 'owner/login.html', {'form': form})
    else:
        form = PropertyOwnerLoginForm()
    return render(request, 'owner/login.html', {'form': form})





def upload_property(request):
    key = request.session.get("session_key")
    if key:
        owner = PropertyOwner.objects.get(phone=key)
        if request.method == 'POST':
            form = PropertyForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.owner = owner 
                form.save()
                messages.success(request, "Property uploaded successfully")
                return render(request, 'html/home.html')
            else:
                messages.error(request, "Form is invalid")
        else:
            form = PropertyForm()
    else:
        messages.error(request, "User session not found")
        return redirect('owner_login')
    
    return render(request, 'owner/upload_property.html', {'form': form, 'user':owner})