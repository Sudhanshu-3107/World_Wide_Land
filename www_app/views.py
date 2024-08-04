from django.shortcuts import render, redirect
from .models import PropertyOwner, Property, PropertyQuery, PropertySeeker, Inquiry, Agent, Feedback
from django.contrib.auth import logout as django_logout
from .forms import  MemberLoginForm, PropertyQueryForm, SeekerLoginForm, SeekerRegisterForm
from django.contrib import messages



def home(request):
    user_details = request.session.get("session_key")
    property = Property.objects.all()
    user_obj = None
    if user_details:
        try:
            user_obj = PropertyOwner.objects.get(phone=user_details)
        except PropertyOwner.DoesNotExist:
            try:
                user_obj = PropertySeeker.objects.get(phone=user_details)
            except PropertySeeker.DoesNotExist:
                return render(request, 'html/home.html', {'properties':property})
    return render(request, 'html/home.html', {'user':user_obj, 'properties':property})


def success_page(request):
    return render(request, 'html/success_page.html')



def member_home(request):
    property = Property.objects.all()
    property_query = PropertyQuery.objects.all()
    property_seeker = PropertySeeker.objects.all()
    owners = PropertyOwner.objects.all()
    inquiry = Inquiry.objects.all()
    context = {
        'property':property,
        'queries':property_query,
        'seekers':property_seeker,
        'owners' : owners,
        'inquiry':inquiry
    }
    return render(request, 'member/home.html', context)



def member_login(request):
    if request.method == 'POST':
        form = MemberLoginForm(request.POST)
        if form.is_valid():
            return redirect('member_home')
    else:
        form = MemberLoginForm()
    
    return render(request, 'member/login.html', {'form': form})





def property_query(request):
    if request.method == 'POST':
        form = PropertyQueryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Query Submitted Successfully')
            return redirect('home')
    else:
        form = PropertyQueryForm()
    return render(request, 'html/query.html', {'form': form})



def inquiry(request, id):
    property = Property.objects.get(id = id)
    key = request.session.get("session_key")
    seeker = None
    if key:
        try:
            seeker = PropertySeeker.objects.get(phone=key)
        except:
            return redirect('seeker_login')
    if seeker:
        if request.method == 'POST':
            key = request.session.get("session_key")
            seeker = PropertySeeker.objects.get(phone=key)
            property = Property.objects.get(id = id)
            ques = request.POST['question']
            obj = Inquiry()
            obj.property = property
            obj.seeker  = seeker
            obj.question = ques
            obj.save()
            messages.success(request, 'Inquiry Sent Successfully')
            return redirect('home')
        else:
            return render(request, 'html/inquiry.html', {'p':property})
    else:
        return redirect('seeker_login')



def seeker_login(request):
    if request.method == 'POST':
        form = SeekerLoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            try:
                seeker = PropertySeeker.objects.get(phone=phone, password=password)
                request.session["session_key"] = phone
                return redirect('home') 
            except PropertySeeker.DoesNotExist:
                error = "Invalid phone or password. Please try again."
                return render(request, 'html/seeker_login.html', {'form': form, 'error': error})
    else:
        form = SeekerLoginForm()
    return render(request, 'html/seeker_login.html', {'form': form})




def seeker_reg(request):
    if request.method == 'POST':
        form = SeekerRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            pic = form.cleaned_data['pic']
            address = form.cleaned_data['address']


            seeker = PropertySeeker(
                phone=phone,
                password=password,
                name=name,
                email=email,
                pic=pic,
                address=address
            )
            seeker.save() 

            return redirect('seeker_login') 
    else:
        form = SeekerRegisterForm()
    return render(request, 'html/seeker_reg.html', {'form': form})


def agents(request):
    agents = Agent.objects.all()
    return render(request, 'html/agents.html', {'agents':agents})

def properties(request):
    properties = Property.objects.all()
    return render(request, 'html/property.html', {'properties':properties})


def feedback(request):
    if request.method == 'GET':
        return render(request, 'html/home.html')
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        remark = request.POST["remark"]
        obj = Feedback(name=name, email=email,remark=remark)
        obj.save()
        messages.success(request, 'Feedback Sent Succefully')
        return render(request, 'html/home.html')


def logout(request):
    django_logout(request)
    return redirect('home')


