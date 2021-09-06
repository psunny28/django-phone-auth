from django.shortcuts import render, redirect
from accounts.forms import UserRegistrationForm


def register(request):
    context={}
    if request.POST:
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['register_form']=form

    else:
        form=UserRegistrationForm()
        context['register_form']=form
    return render(request, "account/signup.html")


def login_view(request):
    return render(request, "accounts/login.html")