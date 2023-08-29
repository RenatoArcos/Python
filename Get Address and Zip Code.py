# pip install geopy
from geopy.geocoders import Nominatim

# Create the geolocator object with a user-agent
geolocator = Nominatim(user_agent="GeoApiExercises")

# Get the city name from the user
place = input("Enter the city name:  ")

# Geocode the location
location = geolocator.geocode(place)

# Print the gepolocation details
print("\n", location, "\n")

# by clcoding.com