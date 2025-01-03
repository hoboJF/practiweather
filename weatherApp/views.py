from django.shortcuts import render
import requests

def index(request):
    API_KEY = ''
    city = 'Baltimore'
    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        if not city:
            city = 'Baltimore'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    try:
        response = requests.get(url.format(city, API_KEY))
        if response.status_code == 200:
            data = response.json()
            weather_data={
            'city' : city,
            'temperature' : data['main']['temp'],
            'conditions' : data['weather'][0]['description']
        }
        else:
            weather_data={
            'city' : city,
            'temperature' : 'N/A',
            'conditions' : 'City is either not found or the request is invalid'
            }
    except requests.exceptions.RequestException as exception:
        weather_data = {
            'city': city,
            'temperature': 'N/A',
            'conditions': 'Could not connect to weather service'
        }
            
    print(weather_data)
    final_data = {'weather_data' : weather_data}
    return render(request, 'weatherApp/weatherApp.html', final_data)
