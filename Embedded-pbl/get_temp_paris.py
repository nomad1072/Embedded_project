import requests
import sys
from twython import Twython

tweetStr = "Weather sample: ..."

apiKey = 'ff6HFDoRj4ah44rF7BAyOX2dk'
apiSecret = '1G3V9HJPmQAUTwXGymZVxpmKqjBbPlDOYBpjeMnbdL1vk9aosM'
accessToken = '857234169847590914-Q2e9KLqKmJfy8jjABVQdHwIpJuvJSyy'
accessTokenSecret = 'Ef5c1eQ1CiPmzS6dQCAD1J8KsiaDUsOfYZdZSpXjt7TYJ'
r = requests.get("http://api.wunderground.com/api/717b7187716ed40f/forecast/q/India/Chennai.json")
data = r.json()


print "Forecast for the next 4 days in Chennai"
str1 = "Forecast for the next 4 days in Chennai\n"
for day in data['forecast']['simpleforecast']['forecastday']:
	print day['date']['weekday']+":"
	str2 = day['date']['weekday']+":"+"\n"
	print "conditions:",day['conditions']
	str3 = "conditions:"+day['conditions']+"\n"
	print "High:", day['high']['celsius']+"C","Low: ",day['low']['celsius']+"C",''
	str4 = "High:"+ day['high']['celsius']+"C"+"Low: "+day['low']['celsius']+"C"+'\n'

tweetStr = str1 + str2 + str3 + str4
api = Twython(apiKey, apiSecret, accessToken, accessTokenSecret)
api.update_status(status = tweetStr)
print "Tweeted: "+tweetStr