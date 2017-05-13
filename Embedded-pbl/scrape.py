import requests
url = 'https://www.google.co.in'
response = requests.get(url)
html = response.content
print html