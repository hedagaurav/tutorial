from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .forms import UserProfile


# Create your views here.
def home(request):
    name = 'Gaurav Heda'
    args = {'myName': name}
    # here "account" is the name of the folder in templates folder.
    return render(request, 'account/register.html', args)


def user_login(request):
    if request.method == 'POST':
        # form = UserProfile(request.POST)
        # if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(username, password, user)
            # if user is not None:
            #     login(request, user)
            #     print(login(request, user))
            #     return redirect('account:home')
            # else:
            #     print("username or password is incorrect.")

    return render(request, 'account/login.html', {})


def user_logout(requset):
    logout(requset)
    return redirect('account:login')
