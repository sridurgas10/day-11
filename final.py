import threading
import requests
#import json
def get1():
    res=requests.get("https://www.w3schools.com/python/python_intro.asp")
    print(res.status_code)
    #print(res.json())

def get2():

    res=requests.get("https://github.com/sridurgas10/day-11/blob/main/req.py")
    print(res.status_code)
    #print(res.json())

t1=threading.Thread(target=get1())
t2=threading.Thread(target=get2())  

t1.start()
t2.start()

t1.join()
t2.join()

print("done")

