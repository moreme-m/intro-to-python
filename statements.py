weight = 60
height = 16.4
BMI = weight/(height*height)

if BMI <= 18.4:
    print("You are underweight")

elif BMI <=24.9:
    print("You are healthy")   

elif BMI <= 29.9:
    print("You are overweight")  

elif BMI <= 34.9:
    print("You are severely overweight")

elif BMI <= 39.9:
    print("You are obese")      

else :
    print("You are severely obese")  

import datetime
print(datetime.datetime.now())
import calendar
print(calendar.calender(3025))       