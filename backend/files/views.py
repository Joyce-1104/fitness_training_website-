import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Membership, Program, Trainer, FitnessProfile , Consultation
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# =====================================
# Helper: login with email OR username
# =====================================
def get_user(identifier):
    return User.objects.filter(Q(username=identifier) | Q(email=identifier)).first()




# ==============================
# Landing → redirect appropriately
# ==============================
def landing_redirect(request):
    if request.user.is_authenticated:
        return redirect("home")
    return redirect("login")
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "All fields are required")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect("login")

        login(request, user)

        # Redirect to profile setup if not created
        if not FitnessProfile.objects.filter(user=user).exists():
            return redirect("profile_setup")

        return redirect("home")

    return render(request, "login.html")

def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "All fields are required")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            password=password
        )
        user.save()

        login(request, user)
        return redirect("profile_setup")

    return render(request, "register.html")

# ==============================
# LOGOUT
# ==============================
def logout_user(request):
    logout(request)
    return redirect("login")


# ==============================
# PROFILE SETUP
# ==============================

@login_required
def profile_setup(request):
    if FitnessProfile.objects.filter(user=request.user).exists():
        return redirect("home")

    if request.method == "POST":
        age = request.POST.get("age")
        weight = request.POST.get("weight")
        height = request.POST.get("height")
        food = request.POST.get("food_habits")
        goal = request.POST.get("goal")
        interested_program = request.POST.get("interested_program")

        image = request.FILES.get("profile_image")

        
        FitnessProfile.objects.create(
            user=request.user,
            age=age,
            weight=weight,
            height=height,
            food_habits=food,
            goal=goal,
            interested_program = interested_program,
            profile_image=image
        )

        return redirect("home")

    return render(request, "profile_setup.html")

# ==============================
# HOME PAGE
# ==============================
@login_required
def home(request):
    programs = Program.objects.all()[:3]
    memberships = Membership.objects.all()[:3]
    trainers = Trainer.objects.all()[:3]
    return render(request, 'home.html', {
        'programs': programs,
        'memberships': memberships,
        'trainers': trainers,
    })


# ==============================
# OTHER PAGES
# ==============================
@login_required
def membership_page(request):
    return render(request, "membership.html")

@login_required
def programs_page(request):
    return render(request, "programs.html")

@login_required
def trainers_profile(request):
    return render(request, "trainers_profile.html")

@login_required
def contact_page(request):
    return render(request, "contact.html")

@login_required
def report_page(request):
    profile = FitnessProfile.objects.get(user=request.user)
    return render(request, "report.html", {"profile": profile})

@login_required
def blog_page(request):
    return render(request, "blog.html")

@login_required
def sucess_stories(request):
    return render(request , "sucess_stories.html")

@login_required
def book_consult(request):
    if request.method == "POST":
        print("BOOK CONSULT VIEW HIT")  # 👈 add this
        
        phone = request.POST.get("phone")

        if not phone:
            messages.error(request, "Phone number is required")
            return redirect("home")

        Consultation.objects.create(
            user=request.user if request.user.is_authenticated else None,
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
           
        )
        send_mail(
            subject="Consultation Booked - ALMI Fitness",
            message="Thank you for booking a consultation. Our team will contact you soon.",
            from_email=None,
            recipient_list=[request.POST.get("email")],
            fail_silently=True,
        )
        messages.success(request, "Consultation booked successfully")
        return redirect("home")
