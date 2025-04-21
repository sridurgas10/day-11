import asyncio

async def sqr():
    for i in range(1,5):
      print(f"sqr{i}:{i**2}")
      await asyncio.sleep(1)

async def main():
   await asyncio.gather(sqr())     

asyncio.run(main())    

