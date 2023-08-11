import requests

api_key = 'b124cce078944fed8a564940231008'
location = 'New Delhi'
country = 'India'

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&country={country}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)  # Display the fetched data
else:
    print('Weather data not found')
