import random
from secrets import choice
number = 0,1,2,3,4,5,6,7,8,9
point = int(random.choice(number))
person = input("Who do you want to rate?")
print(person,"got",point,"/10")