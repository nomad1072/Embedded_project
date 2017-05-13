import sys
from twython import Twython

tweetStr = "Weather sample: ..."

apiKey = 'ff6HFDoRj4ah44rF7BAyOX2dk'
apiSecret = '1G3V9HJPmQAUTwXGymZVxpmKqjBbPlDOYBpjeMnbdL1vk9aosM'
accessToken = '857234169847590914-Q2e9KLqKmJfy8jjABVQdHwIpJuvJSyy'
accessTokenSecret = 'Ef5c1eQ1CiPmzS6dQCAD1J8KsiaDUsOfYZdZSpXjt7TYJ'

api = Twython(apiKey, apiSecret, accessToken, accessTokenSecret)
api.update_status(status = tweetStr)
print "Tweeted: "+tweetStr