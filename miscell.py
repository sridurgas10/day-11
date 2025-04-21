#1.Double a number
#Write a lambda function to double a number.
numlist=[1,2,3,4,5,6]
data=lambda x:x*2 
for x in numlist:

 print(data(x))

#2.Check if a number is even
#Write a lambda function that returns True if a number is even, else False.
data=lambda x:"True" if x%2==0 else "False"
print(data(3))
print(data(6))

#3.Sort a list of tuples by the second element
#Use lambda in sorted() to sort a list like [(1, 2), (3, 1), (5, 0)] by the second value.
list1=[1,5,7,9]
list2=[6,0,3,5]
n=lambda x:sorted(x)
print(n(list2))

data=zip(list1,n(list2))
print(list(data))



#4.Create a power function
#Write a lambda function that takes a number x and returns x**3.
data=lambda x:x**3
print(data(3))


#5.Use lambda with map()
#Use a lambda function with map() to cube all elements in a list.
numlist=[1,2,3,4,5]
data=map(lambda x:x**2,numlist)
print(list(data))