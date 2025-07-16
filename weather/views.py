from django.shortcuts import render
from .utils import fetch_aqi_data
# Create your views here.

def home(request):
    city = request.GET.get("city", "beijing")
    data = fetch_aqi_data(city)
    return render(request, "home.html", {"data": data, "city": city})

def about(request):
    return render(request, 'about.html', {})