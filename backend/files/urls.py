from django.contrib import admin
from django.urls import path, include
from files import views

urlpatterns = [
    path('', views.landing_redirect, name='landing'),

    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_page, name="register"),
    path("profile-setup/", views.profile_setup, name="profile_setup"),
    path("book-consult/", views.book_consult, name="book_consult"),
    path("home/", views.home, name="home"),
    path("membership/", views.membership_page, name="membership"),
    path("programs/", views.programs_page, name="programs"),
    path("trainers/", views.trainers_profile, name="trainers"),
    path("contact/", views.contact_page, name="contact"),
    path("blog/", views.blog_page, name="blog"),
    path("report/", views.report_page, name="report"),
    path("sucess_stories/",views.sucess_stories,name = "sucess_stories"),
]
