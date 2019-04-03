from django.shortcuts import render


def main_page(request):
    collapse = True
    args = {'collapse': collapse}
    return render(request, 'main.html', args)
