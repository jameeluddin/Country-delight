from django.urls import path, include
from . import views

urlpatterns = [
    path('signUp/', views.signup, name="signupurl"),

]