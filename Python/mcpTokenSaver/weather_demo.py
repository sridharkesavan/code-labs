import requests
import json

# Fetch weather data for Seattle
# First, get the grid point for Seattle
location_url = "https://api.weather.gov/points/47.6062,-122.3321"
headers = {'User-Agent': 'Claude Demo (educational purpose)'}

# Get the forecast URL
location_response = requests.get(location_url, headers=headers)
location_data = location_response.json()
forecast_url = location_data['properties']['forecast']

# Get the actual forecast
forecast_response = requests.get(forecast_url, headers=headers)
forecast_data = forecast_response.json()

# Extract just the key information (efficient!)
periods = forecast_data['properties']['periods'][:3]  # First 3 periods
summary = []

for period in periods:
    summary.append({
        'name': period['name'],
        'temperature': f"{period['temperature']}°{period['temperatureUnit']}",
        'forecast': period['shortForecast']
    })

# Create a nicely formatted summary
weather_summary = "Seattle Weather Forecast\n" + "="*40 + "\n\n"
for s in summary:
    weather_summary += f"{s['name']}: {s['temperature']}\n{s['forecast']}\n\n"

print(weather_summary)

# Save to file
with open("weather_summary.txt", "w", encoding="utf-8") as f:
    f.write(weather_summary)
# ...existing code...
print(f"\n{'='*40}")
print(f"Summary saved!")
print(f"Summary size: {len(weather_summary)} characters")
print(f"Full API response size: {len(json.dumps(forecast_data))} characters")
print(f"Token savings: ~{(len(json.dumps(forecast_data)) - len(weather_summary)) // 4} tokens")
print(f"{'='*40}")
