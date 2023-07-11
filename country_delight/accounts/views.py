from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User, UserProfile
from .forms import UserForm


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                            email=email,
                                            password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, "Account has been created successfully")
            return redirect('signupurl')
        else:
            print("Invalid form")
            print(form.errors)
    else:
        form = UserForm()

    context = {
        "form": form,
    }
    return render(request, 'accounts/signup.html', context)