"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import  pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "api_key=wX9NwuHnZU2ToO7GmGR9uw"
#mbta api call url base
MBTA_API_CALL_URL = MBTA_BASE_URL + '?' + MBTA_DEMO_API_KEY

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    return response_data

def create_url(name):
    """
    Given a location with spaces inbetween words, returns a url that 
    corresponds to a google maps query of that location
    """

    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' 
    for word in name.split():
        url = url + word + '%'

    return url

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    #create url and then grab the json file response
    url = create_url(place_name)
    json = get_json(url)

    #pull latitude and longitude data from json
    lat = json["results"][0]["geometry"]["location"]["lat"]
    lng = json["results"][0]["geometry"]["location"]["lng"]

    return (lat,lng)


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """    
    #query MBTA API for given latitude and longitude
    stops = get_json(MBTA_API_CALL_URL + "&lat=" + str(latitude) + '&lon=' + str(longitude) + '&format=json' )
    
    #pull station name and distance from json object
    station_name = stops["stop"][0]['stop_name']
    distance = stops["stop"][0]['distance']

    return (station_name, distance)


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    location = get_lat_long(place_name)
    nearest_stop = get_nearest_station(location[0],location[1])
    
    return nearest_stop


stop = find_stop_near('Fenway Park')

print 'Station Name: ' + stop[0]
print 'Distance: ' + stop[1] + ' miles'
