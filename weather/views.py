from django.shortcuts import render, redirect
import requests
from datetime import datetime, timedelta
from collections import defaultdict

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather_forecast(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch weather data")
        return None

def search(request):
    return render(request, 'weather/search.html')

def weather_search(request):
    api_key = "YOUR_API_KEY" # Change this wth your api key
    city_name = request.POST.get('city_name')
    forecast_data = get_weather_forecast(city_name, api_key)
    if forecast_data:
        today = datetime.utcnow()
        end_date = today + timedelta(days=3) 
        forecast_data_by_day = defaultdict(list)
        for forecast in forecast_data['list']:
            date_time = datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S')
            if date_time < end_date:
                weather_description = forecast['weather'][0]['description']
                temperature = kelvin_to_celsius(forecast['main']['temp'])
                icon_code = forecast['weather'][0]['icon']
                forecast_data_by_day[date_time.date()].append((
                    {
                        'date_time': date_time,
                        'weather_description': weather_description,
                        'temperature': f"{temperature:.2f}°C"
                    },
                    f"http://openweathermap.org/img/w/{icon_code}.png"
                ))

        return render(request, 'weather/weather_search.html', {
            'city_name': city_name,
            'forecast_data': dict(forecast_data_by_day),
        })
    else:
        return render(request, 'weather/error.html', {'city_name': city_name})