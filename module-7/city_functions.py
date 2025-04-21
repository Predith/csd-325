#Function with two parameters
def location(city, country):
    return f"{city}, {country}"

#Call function three times
location1 = location("Austin", "Texas")
location2 = location("Paris", "France")
location3 = location("Seattle", "Washington")

#Print results
print(location1)
print(location2)
print(location3)