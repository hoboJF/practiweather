from django.shortcuts import render
import requests

def index(request):
    API_KEY = '6d9088870fb8cc3dc6d1ba210bf87c58'
    city = 'Baltimore'
    if request.method == 'POST':
        city = request.POST.get('city', 'Baltimore')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    data = requests.get(url.format(city, API_KEY)).json()
    weather_data={
        'city' : city,
        'temperature' : data['main']['temp'],
        'conditions' : data['weather'][0]['description']
    }
    print(weather_data)
    final_data = {'weather_data' : weather_data}
    return render(request, 'weatherApp/weatherApp.html', final_data)
