from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    name = 'Gaurav Heda'
    args = {'myName': name}
    # here "account" is the name of the folder in templates folder.
    return render(request, 'account/register.html', args)


def login(request):

    context = {}
    return render(request, 'account/login.html', context)


def logout(requset):

    return redirect('account:login')
