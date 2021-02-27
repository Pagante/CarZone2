from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.
def cars(request):
    cars_item= Car.objects.order_by('-created_date')
    model_fields = Car.objects.values_list('model', flat=True).distinct()
    city_fields = Car.objects.values_list('city', flat=True).distinct()
    year_fields = Car.objects.values_list('year', flat=True).distinct()
    body_style_fields = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_fields = Car.objects.values_list('transmission', flat=True).distinct()
    paginator = Paginator(cars_item, 2)
    page = request.GET.get('page')
    pages_cars = paginator.get_page(page)

    data = {
        'cars_item':pages_cars,
        'model_fields':model_fields,
        'city_fields': city_fields,
        'year_fields': year_fields,
        'body_style_fields': body_style_fields,
        'transmission_fields':transmission_fields
    }
    return render(request, 'CarZone2/cars.html', data)


def car_details(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car': single_car
    }
    return render(request, 'CarZone2/car_details.html', data)

def search(request):
    search_car = Car.objects.order_by('-created_date')

    model_fields = Car.objects.values_list('model', flat=True).distinct()
    city_fields = Car.objects.values_list('city', flat=True).distinct()
    year_fields = Car.objects.values_list('year', flat=True).distinct()
    body_style_fields = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_fields = Car.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        if keyword:
            search_car = search_car.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']

        if model:
            search_car = search_car.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']

        if city:
            search_car = search_car.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']

        if year:
            search_car = search_car.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']

        if body_style:
            search_car = search_car.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            search_car = search_car.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'search_car':search_car,
        'model_fields':model_fields,
        'city_fields': city_fields,
        'year_fields': year_fields,
        'body_style_fields': body_style_fields,
        'transmission_fields':transmission_fields,
    }
    return render(request, 'CarZone2/search.html', data)
