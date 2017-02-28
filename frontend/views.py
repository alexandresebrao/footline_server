from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'register.html')


def admin(request):
    return render(request, 'admin.html')


def homepage(request):
    return render(request, 'homepage.html')
