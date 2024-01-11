from django.shortcuts import render
from .brain import get_weather

# Create your views here.

def homeview(request) :
    if request.method == "POST":
        api_key = "37216b63a92c35f827dbea0f18e96b29"
        city = request.POST['city']
        print(city)
        result = get_weather(api_key,city)
        print(result)
        context = result
        return render(request, 'weather.html', context = context)

    return render(request, 'homepage.html')


def weatherview(request) :
    return render(request, 'weather.html', {})