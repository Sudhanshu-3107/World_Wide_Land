from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import AgentLoginForm, AgentRegistrationForm
from .models import *

def agent_register(request):
    if request.method == 'POST':
        form = AgentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agent_login')
    else:
        form = AgentRegistrationForm()
    return render(request, 'agent/register.html', {'form': form})

def agent_login(request):
    if request.method == 'POST':
        form = AgentLoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')
            user_list = Agent.objects.filter(phone=phone, password=password)
            size = len(user_list)
            if size>0:
                request.session["session_key"] = phone
                return redirect('agent_home')
            else:
                messages.error(request, 'Wrong Credentials')
                return render(request, 'agent/login.html', {'form': form})
    else:
        form = AgentLoginForm()
    return render(request, 'agent/login.html', {'form': form})


def agent_home(request):
    key = request.session.get('session_key')
    if key:
        user = Agent.objects.get(phone=key)
        inquiry = Inquiry.objects.all()
        queries = PropertyQuery.objects.all()
        properties = Property.objects.all()
        owners = PropertyOwner.objects.all()
        seekers = PropertySeeker.objects.all()
        context = {
            'user':user,
            'inquiry':inquiry,
            'queries':queries,
            'properties':properties,
            'owners':owners,
            'seekers':seekers
        }
        return render(request, 'agent/home.html', context)
    else:
        return redirect('agent_login')