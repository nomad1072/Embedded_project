import urllib2 
import json 
f = urllib2.urlopen('http://api.wunderground.com/api/717b7187716ed40f/geolookup/conditions/q/IA/Cedar_Rapids.json') 
json_string = f.read() 
parsed_json = json.loads(json_string) 
location = parsed_json['display_location']['city'] 
temp_f = parsed_json['current_observation']['temp_f'] 
print "Current temperature in %s is: %s" % (location, temp_f) 
f.close()