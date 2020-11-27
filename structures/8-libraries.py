import math
data = 21.6
print('The floor of 21.6 is:', math.floor(data))

import re
txt = "My twitter username is <username>"
print(re.sub('<username>', '@alesanchezr', txt))

from datetime import datetime, timedelta
current_datetime = datetime.now()
print("Current date ", current_datetime)
# date after 20 days
future_date = current_datetime + timedelta(days=20)
print("future_date date ", future_date)

import json
person = {
    "first_name": "Bob",
    "last_name": "Dylan",
}
serialized = json.dumps(person)
print("Person as ", type(serialized), serialized)
dictionary = json.loads(serialized)
print("Person as ", type(dictionary), dictionary)

import random 
x = random.randint(1, 100)
print("Random between 1 and 100",x)


# import os
# os.mkdir("./apps/thank-you")    
# _list = os.listdir("./") 
# print(_list)

import io
file = io.open("./apps/thank-you/template.txt", "w+", buffering = 5)
print(file.write('I just finished my presentation at the Pycon Chile!\nHere is the presentation and thank you to everyone that followed.'))
file.close()