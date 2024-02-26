import requests
def get_weather_data(api_key, location_name=None, latitude=None, longitude=None, units="metric"): 
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    if location_name:
        complete_url = f"{base_url}?q={location_name}&appid={api_key}&units={units}"
    
    elif latitude is not None and longitude is not None:
        complete_url = (f"{base_url}?lat={latitude}&lon{longitude}&appid={api_key}&units={units}")
        
    else:
        raise ValueError("Either a location name or latitude and longitude must be provided.") 
    response = requests.get(complete_url)
    
    if response.status_code == 200: 
        weather_data = response.json()
        location = weather_data.get("name", "Unknown location")
        temperature = (weather_data["main"]["temp"] if "main" in weather_data else "No data") 
        wind_speed = (weather_data["wind"]["speed"] if "wind" in weather_data else "No data")
        visibility = (weather_data["visibility"] if "visibility" in weather_data else "No data") 
        return location, temperature, wind_speed, visibility
    else:
        return "Error", response.status_code
    
api_key = "59162fe027cff00d1eec35009e240ad0" 
location_name = "London"
location, temperature, wind_speed, visibility = get_weather_data(api_key, location_name=location_name) 

print(f"Location: {location}")
print(f"Temperature: {temperature} C" )
print(f"Wind Speed: {wind_speed} meter/sec")
print(f"Visibility: {visibility} meters")
