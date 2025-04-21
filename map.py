#Convert temperatures
#Given a list of temperatures in Celsius, use map() to convert them to Fahrenheit.
celsius=[0,20,47,200]
fahrenheit=map(lambda c:((c * 9/5) + 32),celsius)

print(list(fahrenheit))


#Capitalize names
#Given a list of names in lowercase, use map() to return a list of capitalized names.
name=['sri','naresh','lithiksha']
data=map(str.upper,name)
print(list(data))


#3.Square each number
#Use map() to return a list where each element is the square of the original list of numbers.
list1=[2,3,4,7,8]
data=map(lambda x: x**2 ,list1)
print(list(data))

#4.Convert strings to integers
#Given a list of numeric strings, use map() to convert them to integers
numlist=['1','2','3','4','5','6','7','8','9']
data=map(int,numlist)
print(list(data))


#5.Add a fixed number to each item
#Add 10 to each element of a given list using map().
numlist=[1,2,3,4,9]
data=map(lambda x:x*10,numlist)
print(list(data))