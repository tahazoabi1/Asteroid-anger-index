import requests
import json
from graphshow import showing_graph
from dangerCal import calculate_danger, user_input

# Replace 'YOUR_API_KEY' with your actual NASA API key
API_KEY = 'm2njjNiLJQbiZxSxAgXmLxJmfaEIfbSDcEDOtNjg'

url = "https://api.nasa.gov/neo/rest/v1/feed"

START_DATE = "2024-03-6"
END_DATE = "2024-03-13"

# Set up the parameters for the API request
params = {'api_key': API_KEY, 'start_date': START_DATE, 'end_date': END_DATE}

data = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={START_DATE}&end_date={END_DATE}&api_key={API_KEY}').json()

with open('data.json', 'w') as file:
    json.dump(data, file)
    print(data['near_earth_objects'])
    processed_results = []
    for date in data['near_earth_objects']:
        asteroids = data['near_earth_objects'][date]
        for asteroid in asteroids:
            processed_asteroid = {
                'id': asteroid['id'],
                'name': asteroid['name'],
                'est_diameter_min': float(asteroid['estimated_diameter']['kilometers']['estimated_diameter_min']),
                'est_diameter_max': float(asteroid['estimated_diameter']['kilometers']['estimated_diameter_max']),
                'miss_distance_km': float(asteroid['close_approach_data'][0]['miss_distance']['kilometers']),
                'relative_velocity_kph': float(asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
            }
            processed_results.append(processed_asteroid)
    with open('processed_data.json', 'w') as file:
        json.dump(processed_results, file, indent=2)

showing_graph(processed_results[1])

A, B, C = user_input()
calculate_danger(processed_results[1], A, B, C)
