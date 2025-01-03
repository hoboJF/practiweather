from django.shortcuts import render
import requests

def index(request):
    ip_address = requests.get('http://api.ipify.org').text
    ip_data = requests.get(f'http://ip-api.com/json/{ip_address}').json()
    location_data={
        'city' : ip_data['city'],
        'region' : ip_data['regionName'],
        'country' : ip_data['country']
    }
    API_KEY = ''
    city = f"{location_data['city']}, {location_data['region']}, {location_data['country']}"
    print(city)
    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        if not city:
            city = f"{location_data['city']}, {location_data['region']}, {location_data['country']}"
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
