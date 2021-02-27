from django.shortcuts import render
from .models import Team
from CarZone2 .models import Car
# Create your views here.
def home(request):
    teams = Team.objects.all()
    feature_cars= Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    data = {
        'teams':teams,
        'feature_cars':feature_cars,
        'all_cars':all_cars
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')



def contacts(request):
    return render(request, 'pages/contact.html')
