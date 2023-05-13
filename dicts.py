from pprint import pprint as print

place = {"city": "Москва", "temperature": 20}
print(place["city"])
place["temperature"] -= 5
print(place)

# print(place['country']) # KeyERROR 
print(place.get("country", "Россия"))
place["date"] = "27.05.2019"
print(len(place))
