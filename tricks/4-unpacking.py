# Lambdas are pyhton arrow functions

a = ["alesanchezr", "Alejandro", "Sanchez"] 

twitter, first_name = a
print(twitter)
print(first_name)


_dict = { "twitter": "alesanchezr", "first_name": "Alejandro" }
print("Keys:", *_dict)


_dict2 = { "last_name": "Sanchez" }
merged = { **_dict, **_dict2 }
print(merged)
