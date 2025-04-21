#1.Sum of all elements
#Use reduce() to compute the sum of all numbers in a list.
from functools import reduce
list1=[1,4,8,5,23]
data=reduce(lambda x,y:x+y,list1)
print(data)

from functools import reduce
list1=[1,4,8,5,23]
def add(x,y):
   return x+y
data=reduce(add,list1)
print(data)



#2.Product of all elements
#Use reduce() to compute the product of all elements in a list.
from functools import reduce
list1=[1,4,8,5,23]
data=reduce(lambda x,y:x*y,list1)
print(data)

#3.Find the maximum number
#Use reduce() to find the maximum number in a list.
from functools import reduce
list1=[1,4,8,5,23]

data=reduce(lambda x,y: x if x>y else y,list1)
print(data)


#4.Concatenate all strings
#Given a list of strings, use reduce() to concatenate them into a single string.
import functools 
import operator
strlist=["sri","durga","naresh"]
print(functools.reduce(operator.add,strlist))


#5.Compute factorial
#Use reduce() to compute the factorial of a number n, using range(1, n+1).
from functools import reduce

factorial=reduce(lambda x,y:x*y,  range(1,5))

print(factorial)

