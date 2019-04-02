from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):

    name = 'Gaurav Heda'
    args = {'myName': name}
    # here "account" is the name of the folder in templates folder.
    return render(request, 'account/home.html', args)
