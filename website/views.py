from django.shortcuts import render, get_object_or_404, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as dj_login, logout



# Create your views here.
def index(request):
    banner = Results_banner.objects.all()
    about = About.objects.all()
    contest = Contest.objects.all()
    testimonial = Testimonial.objects.all()
    context = {
        "banner":banner,
        "about" : about,
        "contest" : contest,
        "testimonial" : testimonial,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    data = About.objects.all()
    context = {
        "data":data
    }
    return render(request, 'pages/about.html', context)


def contest(request):
    data = Contest.objects.all()
    context = {
        "data":data,
    }
    return render(request, 'pages/contest.html', context)

def contact(request):
    return render(request, 'pages/contact.html')


def singleContest(request, slug):
    contest = get_object_or_404(Contest, slug=slug)
    user = request.user

    # Check if the user has submitted a logo for this contest
    has_Submitted = SubmitLogo.objects.filter(user=user, contest=contest).exists()
    has_joined = JoinContest.objects.filter(user=user, contest=contest).exists()

    context = {
        "contest": contest,
        "has_joined": has_joined,
        "has_submitted": has_Submitted,
    }

    return render(request, 'pages/contest-detail.html', context)


def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        fpassword = make_password(password)

        user = User.objects.create(username=email, password=fpassword, email=email, first_name=name)  # Use hashed_password
        user.save()

        # login
        dj_login(request, user)
        return redirect('/contest')
    return render(request, 'pages/register.html')    


def login(request):
    if request.method == "POST":
        loginusername = request.POST['username']
        loginpassword = request.POST["password"]

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            dj_login(request, user)
            return redirect('/contest')
        else:
            return redirect('/login')
    
    return render(request, 'pages/login.html')