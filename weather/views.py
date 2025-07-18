from django.shortcuts import render
from .utils import fetch_aqi_data
# Create your views here.

def home(request):
    city = request.GET.get("city", "beijing").strip()
    area = request.GET.get("area", "").strip()
    feed = f"{city}/{area}" if area else city
    data = fetch_aqi_data(feed)
    return render(request, "home.html", {"data": data, "city": city, "area": area})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def table(request):
    return render(request, 'table.html', {})