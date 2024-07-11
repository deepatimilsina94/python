# 'Day 2: 30 Days of python programming'
first_name = "Deepa"
last_name = "Timilsina"
full_name = "Deepa Timilsina" 
country = "Nepal"
city = "Kathmandu"
age = 30
year = 1994
is_married = True
is_true = True
is_light_on = False
color, number, book = "blue", 7, "math"
print(type(first_name))
print(type(last_name))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
first_name_length = len(first_name)
print(first_name_length)
last_name_length = len(last_name)
print(last_name_length)
if first_name_length > last_name_length:
    print("First name is longer than last name")
elif first_name_length < last_name_length:
    print("last name is longer")
else:
    print("both are equal")
num_one = 5
num_two = 4
total = num_one + num_two
print("Total:", total)
import math
radius = 30
_area_of_circle = math.pi * radius**2
print("Area of circle:", _area_of_circle)

user_radius = int(input("Enter the radius of the circle: "))
user_area_of_circle = math.pi * user_radius**2
print("Area of the circle with radius", user_radius, "is:", user_area_of_circle)
name = input("enter full name")
print("name of the student", name)
age = int(input(" enter age of the student:"))
print("age of the student:", age)
help("keywords")
a = 5
b = 10
add = a + b
print("addition", add)
is_sunny = True
is_rainy = False
result = is_sunny and is_rainy
print(result)
result = is_sunny or is_rainy
print(result)