#String formatting using .format()
radius=4.5
area=3.14*radius**2
str="The area of circle with r={} is {}".format(radius,area)
print(str)

#f-strings
str1=f'The area of circle with radius={radius} is {area}'
print(str1)

#Strings are sequence of characters, they can be accessed using -
#1.Unpacking
fruit='Apple'
a,b,c,d,e=fruit
print(a,b,c,d,e)

#2.Accessing by index - from 0 to len-1
print(fruit[2])
#fruit[0]='b' gives TypeError because strings are immutable

#3.Strings as iterable
for i in fruit:
    print(i)

#4.Slicing
personal_info="Hey this is Bipasha Panwar. I am in final year of BTech."
print(personal_info[1:8]) #(included) start:stop (excluded)
print(personal_info[::3]) #start:stop:step

#Reverse string using slicing
print(fruit[::-1])


