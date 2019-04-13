from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import reverse
from .forms import UserProfile1, UserRegistrationForm


# Create your views here.
@login_required
def user_home(request):
    name = 'Gaurav Heda'
    args = {'myName': name}
    # here "account" is the name of the folder in templates folder.
    return render(request, 'account/home.html', args)


def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            pass

    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'account/register.html', context)


def user_login(request):
    form = UserProfile1()
    if request.method == 'POST':
        form = UserProfile1(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(username, password, user)
            if user is not None:
                login(request, user)
                print(login(request, user))
                return redirect(reverse('account:account_home'))
            else:
                message = "username or password is incorrect."
                messages.error(request, message)
                form = UserProfile1()
    context = {'form': form}
    return render(request, 'account/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('account:login')
