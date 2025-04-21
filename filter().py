#1.Filter even numbers
#Use filter() to return only the even numbers from a list.
numlist=[1,2,3,4,5,6,7,8,9]
even_numbers=filter(lambda x:x%2==0,numlist)
print(list(even_numbers))

#2.Filter names starting with a specific letter
#Given a list of names, filter the ones that start with the letter "A".
strlist1=["sri","ant","durga","angel","lithi","apple"]
#strlist=filter(str.startwith('a'),strlist)
strlist2=filter(lambda x:x[0]=='a',strlist1)
print(list(strlist2))


#3.Filter positive numbers
#Use filter() to return only the positive numbers from a list.
numlist=[0,1,-5,4,-7,9,-8]
pos_num=filter(lambda x:x>0, numlist)
print(list(pos_num))

#4.Filter strings longer than 5 characters
#From a list of strings, filter out those that have more than 5 characters
strlist=["sri","lithiksha","durga","naresh","selvaraj"]
data=filter(lambda x:len(x)>5,strlist)
print(list(data))


#5.Filter palindromes
#Given a list of strings, use filter() to return only the palindromes
strlist=["mom","sri","level","durga","radar","naresh","eye"]
data=filter(lambda x:x ==x[::-1],strlist)
print(list(data))