import asyncio
import requests


async def get1():
    res=requests.get("https://www.w3schools.com/python/python_intro.asp")
    print(res.status_code)
    await asyncio.sleep(1)

async def get2():
    res=requests.get("https://github.com/sridurgas10/day-11/blob/main/req.py")
    print (res.status_code)  
    await asyncio.sleep(1)


async def get3():
    res=requests.get("https://github.com/sridurgas10/day-11")
    print (res.status_code)  
    await asyncio.sleep(1)
 
async def main():     
    await asyncio.gather(get1(),get2(),get3())
asyncio.run(main())    