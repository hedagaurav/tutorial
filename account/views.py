from django.shortcuts import render


# Create your views here.
def home(request):

    name = 'Gaurav Heda'
    args = {'myName': name}
    # here "account" is the name of the folder in templates folder.
    return render(request, 'account/register.html', args)
